import random
import re
import string

def generate(mercosul: bool = False) -> str:
    """
    Generate a valid Brazilian vehicle plate.

    Args:
        mercosul (bool): If True, generates a Mercosul-style plate (ABC1D23).
                         If False, uses the traditional format (ABC-1234).

    Returns:
        str: Valid vehicle plate.
    """
    letters = ''.join(random.choices(string.ascii_uppercase, k=3))

    if mercosul:
        num1 = str(random.randint(0, 9))
        letter = random.choice(string.ascii_uppercase)
        num2 = ''.join(str(random.randint(0, 9)) for _ in range(2))
        return f"{letters}{num1}{letter}{num2}"
    else:
        numbers = ''.join(str(random.randint(0, 9)) for _ in range(4))
        return f"{letters}-{numbers}"

def validate(plate: str) -> bool:
    """
    Validate a Brazilian vehicle plate in either format.

    Args:
        plate (str): Plate to validate.

    Returns:
        bool: True if valid format, False otherwise.
    """
    plate = plate.upper()

    old_format = re.fullmatch(r'[A-Z]{3}-?\d{4}', plate)
    mercosul_format = re.fullmatch(r'[A-Z]{3}\d[A-Z]\d{2}', plate)

    return bool(old_format or mercosul_format)
