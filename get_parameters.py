from blockfrost import BlockFrostApi, ApiError, ApiUrls
from pprint import pprint
import json
import argparse

api = BlockFrostApi(
    project_id = "sanchonetQvnETPNwzx19qHeEX4tmfNWAM6lUbhZM",
    base_url='https://cardano-sanchonet.blockfrost.io/api'
)

try:
    # Get the latest epoch number
    latest_epoch = api.epoch_latest()
    print(latest_epoch.to_dict())
    latest_epoch = latest_epoch.to_dict()["epoch"]
    for epoch in range(292,latest_epoch+1):
        # Get the current protocol parameters
        parameters = api.epoch_protocol_parameters(epoch)
        parameters_dict = parameters.to_dict()
        pprint(parameters_dict)
        if parameters_dict["epoch"] >= 290:
            parameters_dict["cost_models"] = parameters_dict["cost_models"].to_dict()
            if "PlutusV1" in parameters_dict["cost_models"]:
                parameters_dict["cost_models"]["PlutusV1"] = parameters_dict["cost_models"]["PlutusV1"].to_dict()
            if "PlutusV2" in parameters_dict["cost_models"]:
                parameters_dict["cost_models"]["PlutusV2"] = parameters_dict["cost_models"]["PlutusV2"].to_dict()
            if "PlutusV3" in parameters_dict["cost_models"]:
                parameters_dict["cost_models"]["PlutusV3"] = parameters_dict["cost_models"]["PlutusV3"].to_dict()
        print(type(parameters))
        with open(f'./constitutions/constitution_test_{parameters_dict["epoch"]}.json', 'w') as f:
            json.dump(parameters_dict, f)
except ApiError as e:
    pprint(e)