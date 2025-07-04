import random
import re

def generate(masked: bool = False) -> str:
    """
    Generate a random Brazilian RG number (9 digits).
    
    Args:
        masked (bool): If True, returns RG formatted as "XX.XXX.XXX-X".
    
    Returns:
        str: Generated RG number, masked or unmasked.
    """
    digits = [str(random.randint(0, 9)) for _ in range(8)]
    
    last_digit = random.choice([str(random.randint(0,9)), 'X'])
    digits.append(last_digit)
    
    rg = ''.join(digits)
    
    if masked:
        rg = f"{rg[:2]}.{rg[2:5]}.{rg[5:8]}-{rg[8]}"
        
    return rg

def validate(rg: str) -> bool:
    """
    Strictly validate a Brazilian RG number.

    Accepts only two formats:
    - Unmasked: 9 characters, digits + optional 'X' as last character
    - Masked: format "XX.XXX.XXX-X"

    Args:
        rg (str): RG number, masked or unmasked.

    Returns:
        bool: True if format and content are valid, False otherwise.
    """
    rg = rg.upper()

    unmasked_pattern = r'^\d{8}[\dX]$'

    masked_pattern = r'^\d{2}\.\d{3}\.\d{3}-[\dX]$'

    return bool(re.fullmatch(unmasked_pattern, rg) or re.fullmatch(masked_pattern, rg))