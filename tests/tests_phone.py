import re
import pytest
from brpack import phone

def test_generate_unmasked_mobile():
    """Testa geração de celular sem máscara."""
    ph = phone.generate(mobile=True, masked=False)
    assert re.fullmatch(r'\d{11}', ph)
    assert phone.validate(ph)

def test_generate_unmasked_landline():
    """Testa geração de fixo sem máscara."""
    ph = phone.generate(mobile=False, masked=False)
    assert re.fullmatch(r'\d{10}', ph)
    assert phone.validate(ph)

def test_generate_masked_mobile():
    """Testa geração de celular com máscara."""
    ph = phone.generate(mobile=True, masked=True)
    assert re.fullmatch(r'\(\d{2}\) 9\d{4}-\d{4}', ph)
    assert phone.validate(ph)

def test_generate_masked_landline():
    """Testa geração de fixo com máscara."""
    ph = phone.generate(mobile=False, masked=True)
    assert re.fullmatch(r'\(\d{2}\) [2-5]\d{3}-\d{4}', ph)
    assert phone.validate(ph)

@pytest.mark.parametrize("valid_phone", [
    "(11) 91234-5678", "11912345678",
    "(21) 2345-6789",  "2123456789",
])
def test_validate_valid_examples(valid_phone):
    """Testa telefones válidos conhecidos."""
    assert phone.validate(valid_phone)

@pytest.mark.parametrize("invalid_phone", [
    "00000000000",
    "(99) 11234-5678",
    "(11) 81234-5678",
    "(11) 1234-5678",
    "1191234567",
    "(11 91234-5678",
    "",
    "112345678901",
])
def test_validate_invalid_examples(invalid_phone):
    """Testa telefones inválidos que devem falhar."""
    assert not phone.validate(invalid_phone)
