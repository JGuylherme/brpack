import random
import re

def generate(masked: bool = False) -> str:
    """
    Generate a valid Brazilian Voter Registration Number (Título de Eleitor).
    
    Args:
        masked (bool): If True, returns formatted title (e.g. '1234.5678.9012')
    
    Returns:
        str: Valid voter ID.
    """
    number = [random.randint(0, 9) for _ in range(8)]

    uf = random.randint(1, 28)
    number.append(uf // 10)
    number.append(uf % 10)

    def calc_dv(nums, weights):
        total = sum(n * w for n, w in zip(nums, weights))
        rest = total % 11
        return 0 if rest == 10 else rest

    d1 = calc_dv(number, list(range(2, 11)))
    number.append(d1)

    d2 = calc_dv(number, list(range(3, 12)))
    number.append(d2)

    digits = ''.join(str(n) for n in number)
    
    if masked:
        return f"{digits[:4]}.{digits[4:8]}.{digits[8:]}"
    
    return digits

def validate(titulo: str) -> bool:
    """
    Validate a Brazilian Voter Registration Number.
    
    Args:
        titulo (str): Title number, masked or unmasked.
    
    Returns:
        bool: True if valid, False otherwise.
    """
    titulo = re.sub(r'\D', '', titulo)
    
    if len(titulo) != 12:
        return False
    
    try:
        nums = [int(c) for c in titulo]
    except ValueError:
        return False

    uf = int(titulo[8:10])
    if uf < 1 or uf > 28:
        return False

    def calc_dv(nums, weights):
        total = sum(n * w for n, w in zip(nums, weights))
        rest = total % 11
        return 0 if rest == 10 else rest

    d1 = calc_dv(nums[:10], list(range(2, 11)))
    d2 = calc_dv(nums[:11], list(range(3, 12)))

    return nums[10] == d1 and nums[11] == d2
