import random
import re

def generate(masked: bool = False) -> str:
    """
    Generate a valid Brazilian CNPJ number.

    Args:
        masked (bool): If True, returns CNPJ with mask (##.###.###/####-##). Default is False.

    Returns:
        str: A valid CNPJ number, masked or unmasked.
    """
    def calculate_digit(digits):
        """
        Calculate one of the two verification digits for CNPJ.
        """
        weights = [6,5,4,3,2,9,8,7,6,5,4,3,2]
        s = sum(int(d) * w for d, w in zip(digits, weights[-len(digits):]))
        d = 11 - s % 11
        return str(d if d < 10 else 0)

    digits = [str(random.randint(0, 9)) for _ in range(12)]
    digits.append(calculate_digit(digits))
    digits.append(calculate_digit(digits))

    cnpj = ''.join(digits)
    if masked:
        return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"
    return cnpj

def validate(cnpj: str) -> bool:
    """
    Validate a Brazilian CNPJ number.

    Args:
        cnpj (str): The CNPJ to validate, masked or unmasked.

    Returns:
        bool: True if valid, False otherwise.
    """
    cnpj = re.sub(r'\D', '', cnpj)

    if len(cnpj) != 14 or cnpj == cnpj[0] * 14:
        return False

    def calculate_digit(digits):
        """
    Calculate one verification digit for CNPJ.
    """
        weights = [6,5,4,3,2,9,8,7,6,5,4,3,2]
        s = sum(int(d) * w for d, w in zip(digits, weights[-len(digits):]))
        d = 11 - s % 11
        return str(d if d < 10 else 0)

    first_digit = calculate_digit(cnpj[:12])
    second_digit = calculate_digit(cnpj[:13])

    return cnpj[12] == first_digit and cnpj[13] == second_digit