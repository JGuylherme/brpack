import re
import requests
import time

def validate(cep: str) -> bool:
    """
    Validate a Brazilian CEP (postal code).

    Args:
        cep (str): The CEP to validate, masked or unmasked.

    Returns:
        bool: True if the CEP is valid (8 digits), False otherwise.
    """
    cep = re.sub(r'\D', '', cep)
    return bool(re.fullmatch(r'\d{8}', cep))

def format(cep: str) -> str:
    """
    Format a Brazilian CEP into the standard mask "12345-678".

    Args:
        cep (str): The CEP to format, masked or unmasked.

    Returns:
        str: The formatted CEP string.

    Raises:
        ValueError: If the CEP is invalid or not 8 digits long.
    """
    cep = re.sub(r'\D', '', cep)
    if not re.fullmatch(r'\d{8}', cep):
        raise ValueError("Invalid CEP format")
    return f"{cep[:5]}-{cep[5:]}"

def check_cep_exists(cep: str) -> bool:
    """
    Check if a CEP exists by querying the ViaCEP API.

    Args:
        cep (str): CEP in 8-digit format (numbers only).

    Returns:
        bool: True if CEP exists, False if not found or invalid.
    """
    cep = re.sub(r'\D', '', cep)
    if len(cep) != 8:
        return False

    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        # ViaCEP returns {"erro": true} if CEP does not exist
        return not data.get("erro", False)
    except (requests.RequestException, ValueError):
        return False
