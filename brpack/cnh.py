import random
import re

def generate(masked: bool = False) -> str:
    """
    Generate a valid Brazilian CNH number (11 digits).

    Args:
        masked (bool): If True, returns formatted CNH (e.g. '123456789-09')

    Returns:
        str: Valid CNH number.
    """
    base = [random.randint(0, 9) for _ in range(9)]

    s1 = sum([(9 - i) * base[i] for i in range(9)])
    d1 = s1 % 11
    if d1 >= 10:
        d1 = 0
        flag = True
    else:
        flag = False

    s2 = sum([(i + 1) * base[i] for i in range(9)])
    if flag:
        s2 -= 2
    d2 = s2 % 11
    d2 = 0 if d2 >= 10 else d2

    digits = base + [d1, d2]
    cnh = ''.join(map(str, digits))

    if masked:
        return f"{cnh[:9]}-{cnh[9:]}"
    return cnh

def validate(cnh: str) -> bool:
    """
    Validate a Brazilian CNH number.

    Args:
        cnh (str): CNH string, masked or unmasked

    Returns:
        bool: True if valid, False otherwise.
    """
    cnh = re.sub(r'\D', '', cnh)

    if len(cnh) != 11 or cnh == cnh[0] * 11:
        return False

    base = [int(c) for c in cnh[:9]]
    dv_input = cnh[9:]

    s1 = sum([(9 - i) * base[i] for i in range(9)])
    d1 = s1 % 11
    if d1 >= 10:
        d1 = 0
        flag = True
    else:
        flag = False

    s2 = sum([(i + 1) * base[i] for i in range(9)])
    if flag:
        s2 -= 2
    d2 = s2 % 11
    d2 = 0 if d2 >= 10 else d2

    return dv_input == f"{d1}{d2}"
