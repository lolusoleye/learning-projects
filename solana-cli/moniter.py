import requests ,time 

WALLET_ADDRESS = "Vote111111111111111111111111111111111111111p"
RPC_URL = "https://api.mainnet-beta.solana.com"
POLL_INTERVAL = 10


def get_latest_signature(WALLET_ADDRESS):
    requests.post(RPC_URL,WALLET_ADDRESS)


def 