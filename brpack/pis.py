import random
import re

def generate(masked: bool = False) -> str:
    """
    Generate a valid Brazilian PIS number (11 digits).
    
    Args:
        masked (bool): If True, returns formatted PIS (e.g. '123.45678.90-1')
    
    Returns:
        str: Valid PIS number.
    """
    digits = [random.randint(0, 9) for _ in range(10)]
    weights = [3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    total = sum(d * w for d, w in zip(digits, weights))
    remainder = total % 11
    check_digit = 11 - remainder if remainder > 1 else 0
    digits.append(check_digit)

    pis = ''.join(map(str, digits))
    if masked:
        return f"{pis[:3]}.{pis[3:8]}.{pis[8:10]}-{pis[10]}"
    return pis

def validate(pis: str) -> bool:
    """
    Validate a Brazilian PIS number.
    
    Args:
        pis (str): PIS string, masked or unmasked
    
    Returns:
        bool: True if valid, False otherwise.
    """
    pis = re.sub(r'\D', '', pis)
    if len(pis) != 11 or pis == pis[0] * 11:
        return False

    digits = [int(c) for c in pis[:10]]
    check_digit = int(pis[10])
    weights = [3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    total = sum(d * w for d, w in zip(digits, weights))
    remainder = total % 11
    expected = 11 - remainder if remainder > 1 else 0

    return check_digit == expected
