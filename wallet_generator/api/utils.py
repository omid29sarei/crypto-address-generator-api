from eth_account import Account
import secrets


def eth_account_creator() -> str:
    """This function will generate a random 32btyes string to be used as private to generate the addres
    Returns:
        str: return the eth acount address
    """

    priv = secrets.token_hex(32)
    private_key = "0x" + priv
    eth_account = Account.from_key(private_key)
    print("Address:", eth_account.address)
    return eth_account.address


def btc_account_creator() -> str:
    pass


def acronym_handler(acronym: str) -> str:
    if "ETH" in acronym:
        return eth_account_creator()
    elif "BTC" in acronym:
        return btc_account_creator()
