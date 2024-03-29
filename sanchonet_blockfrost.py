from blockfrost import BlockFrostApi, ApiError, ApiUrls

api = BlockFrostApi(
    project_id = "sanchonetQvnETPNwzx19qHeEX4tmfNWAM6lUbhZM",
    base_url='https://cardano-sanchonet.blockfrost.io/api'
)

try:
    health = api.health()
    print(health)
except:
    print("Error")
