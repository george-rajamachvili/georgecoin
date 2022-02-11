from brownie import accounts, config, GeorgeCoin

initial_supply = 1000000000000000000000000 # 1000000
token_name = "GeorgeCoin"
token_symbol = "GEO"

def main():
    account = accounts.add(config["wallets"]["from_key"])
    erc20 = GeorgeCoin.deploy(initial_supply, {"from": account})
