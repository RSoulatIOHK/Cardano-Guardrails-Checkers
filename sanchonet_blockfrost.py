from blockfrost import BlockFrostApi, ApiError, ApiUrls
import pprint
api = BlockFrostApi(
    project_id = "sanchonetQvnETPNwzx19qHeEX4tmfNWAM6lUbhZM",
    base_url='https://cardano-sanchonet.blockfrost.io/api'
)

latest_epoch = api.epoch_latest()
latest_epoch = latest_epoch.to_dict()["epoch"]
for epoch in range(281,282):
    print(f'Epoch: {epoch}')
    block = api.block(1197566)
    transactions = api.block_transactions(1197566)    
    transaction = transactions[0]
    transaction_content = api.transaction(transaction)
    print(transaction_content)