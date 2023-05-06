from web3 import Web3

# Configure web3 provider URL and token here
WEB3_PROVIDER = "https://tinyurl.com/web3provider"

# Connect to Ethereum network
w3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER))

# Check if we succesfully connected to Ethereum network
try:
    w3.is_connected()
except Exception as e:
    print(
        "Not connected to Ethereum network, please check your web3 provider credentials"
    )
    exit(1)

# Set up contract instance for LOOT
LOOT_CONTRACT_ADDRESS = "0xFF9C1b15B16263C61d017ee9F65C50e4AE0113D7"
LOOT_CONTRACT_ABI = [
    {
        "inputs": [{"internalType": "uint256", "name": "tokenId", "type": "uint256"}],
        "name": "getWeapon",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function",
    }
]
loot_contract = w3.eth.contract(address=LOOT_CONTRACT_ADDRESS, abi=LOOT_CONTRACT_ABI)

# Retrieve weapons for Token ID's 1-n
for i in range(1, 5):
    weapon = loot_contract.functions.getWeapon(i).call()
    print(f"Token ID {i}: {weapon}")
