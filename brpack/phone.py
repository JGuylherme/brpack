import random
import re

VALID_DDDS = {
    "11","12","13","14","15","16","17","18","19",
    "21","22","24","27","28",
    "31","32","33","34","35","37","38",
    "41","42","43","44","45","46",
    "47","48","49",
    "51","53","54","55",
    "61","62","63","64","65","66","67","68","69",
    "71","73","74","75","77",
    "79",
    "81","82","83","84","85","86","87","88","89",
    "91","92","93","94","95","96","97","98","99"
}

def generate(mobile: bool = True, masked: bool = False) -> str:
    """
    Generate a Brazilian phone number.

    Args:
        mobile (bool): True for mobile (9 digits), False for landline (8 digits).
        masked (bool): Whether to include máscara "(DD) 9XXXX‑XXXX".

    Returns:
        str: Generated phone number.
    """
    ddd = random.choice(list(VALID_DDDS))
    if mobile:
        num = "9" + "".join(str(random.randint(0,9)) for _ in range(8))
    else:
        num = "".join(str(random.randint(0,9)) for _ in range(8))

    if masked:
        return f"({ddd}) {num[:5]}-{num[5:]}"
    return f"{ddd}{num}"

def validate(phone: str) -> bool:
    """
    Validate a Brazilian phone number.

    Accepts:
    - Unmasked: "DDDNXXXXXXXX" or "DDDXXXXXXXX"
    - Masked: "(DD) 9XXXX-XXXX" or "(DD) XXXX-XXXX"

    Args:
        phone (str): Phone number to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    clean = re.sub(r'\D', '', phone)
    if len(clean) not in (10,11):
        return False

    ddd = clean[:2]
    rest = clean[2:]
    if ddd not in VALID_DDDS:
        return False

    if len(rest) == 9:
        return rest[0] == "9" and rest[1:].isdigit()
    if len(rest) == 8:
        return rest.isdigit() and rest[0] in "2345"
    return False
