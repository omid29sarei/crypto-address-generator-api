import hashlib
import copy
import logging
from pywallet import wallet as w

logger = logging.getLogger(__name__)


def wallet_creator(
    network: str, seed: str = w.generate_mnemonic(), children: int = 1
) -> str:
    """This function will generate a random 32btyes string to be used as private to generate the addres
    Returns:
        str: return the eth acount address
    """
    try:
        seed = w.generate_mnemonic()
        wallet = w.create_wallet(network=network, seed=seed, children=children)
    except Exception as error:
        logger.error(f"Something went wrong with error {error}")
        return False
    return wallet


def SHA256_hash_handler(field: str) -> str:
    """This is a simple handler to hash the input string value

    Args:
        field (str): field to be hashed

    Returns:
        str: hex digest for the input string
    """
    try:
        hash_object = hashlib.sha256(field.encode())
        hex_dig = hash_object.hexdigest()
    except Exception as error:
        logger.error(f"Something went wrong with error {error}")
        return False
    return hex_dig


def encrypt_sensitive_fields(account_details: dict) -> dict:
    """This is a helper function which use SHA256 to encrypt sensitive fields

    Args:
        account_details (dict): This is a dictionary containing all the fields after wallet generated

    Returns:
        dict: return the same structure dictionary with encrypted sensitive data
    """
    new_account_details = copy.deepcopy(account_details)
    seed = new_account_details.get("seed")
    private_key = new_account_details.get("private_key")
    hex_seed = SHA256_hash_handler(seed)
    hex_private_key = SHA256_hash_handler(private_key)
    new_account_details["seed"] = hex_seed
    new_account_details["private_key"] = hex_private_key
    return new_account_details
