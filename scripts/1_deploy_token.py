from brownie import accounts, config, TokenERC20

initial_supply = 1000000000000000000 # 100
token_name = "GeorgeCoin"
token_symbol = "GEO"

def main():
    account = accounts[0]
    erc20 = TokenERC20.deploy(initial_supply, token_name,
        token_symbol, {"from": account})
