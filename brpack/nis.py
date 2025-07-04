import random
import re

def generate(masked: bool = False) -> str:
    """
    Generate a valid Brazilian NIS number (11 digits).
    
    Args:
        masked (bool): If True, returns formatted NIS (e.g. '123.45678.90-1')
    
    Returns:
        str: Valid NIS number.
    """
    digits = [random.randint(0, 9) for _ in range(10)]
    weights = [3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    total = sum(d * w for d, w in zip(digits, weights))
    remainder = total % 11
    check_digit = 11 - remainder if remainder > 1 else 0
    digits.append(check_digit)

    nis = ''.join(map(str, digits))
    if masked:
        return f"{nis[:3]}.{nis[3:8]}.{nis[8:10]}-{nis[10]}"
    return nis

def validate(nis: str) -> bool:
    """
    Validate a Brazilian NIS number.
    
    Args:
        nis (str): NIS string, masked or unmasked
    
    Returns:
        bool: True if valid, False otherwise.
    """
    nis = re.sub(r'\D', '', nis)
    if len(nis) != 11 or nis == nis[0] * 11:
        return False

    digits = [int(c) for c in nis[:10]]
    check_digit = int(nis[10])
    weights = [3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    total = sum(d * w for d, w in zip(digits, weights))
    remainder = total % 11
    expected = 11 - remainder if remainder > 1 else 0

    return check_digit == expected
