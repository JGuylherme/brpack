import random
import re

def generate(masked: bool = False) -> str:
    """
    Generate a valid Brazilian CPF number.

    Args:
        masked (bool): If True, returns CPF with mask (###.###.###-##). Default is False.

    Returns:
        str: A valid CPF number, masked or unmasked.
    """
    def calculate_digit(digits):
        """
        Calculate one of the two verification digits for CPF.
        """
        s = sum(int(d) * w for d, w in zip(digits, range(len(digits) + 1, 1, -1)))
        d = 11 - s % 11
        return str(d if d < 10 else 0)

    digits = [str(random.randint(0, 9)) for _ in range(9)]
    digits.append(calculate_digit(digits))
    digits.append(calculate_digit(digits))

    cpf = ''.join(digits)
    if masked:
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    return cpf

def validate(cpf: str) -> bool:
    """
    Validate a Brazilian CPF number.

    Args:
        cpf (str): The CPF to validate, masked or unmasked.

    Returns:
        bool: True if valid, False otherwise.
    """
    cpf = re.sub(r'\D', '', cpf)

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    def calculate_digit(digits):
        """
        Calculate one of the two verification digits for CPF.
        """
        s = sum(int(d) * w for d, w in zip(digits, range(len(digits) + 1, 1, -1)))
        d = 11 - s % 11
        return str(d if d < 10 else 0)

    first_digit = calculate_digit(cpf[:9])
    second_digit = calculate_digit(cpf[:10])

    return cpf[9] == first_digit and cpf[10] == second_digit
