import pytest
from brpack import pis

def test_generate_unmasked():
    """Testa geração de PIS não formatado."""
    number = pis.generate(masked=False)
    assert isinstance(number, str)
    assert len(number) == 11
    assert pis.validate(number), f"Generated PIS {number} should be valid"

def test_generate_masked():
    """Testa geração de PIS formatado."""
    number = pis.generate(masked=True)
    assert isinstance(number, str)
    assert len(number) == 14
    assert pis.validate(number), f"Generated masked PIS {number} should be valid"

@pytest.mark.parametrize("valid_pis", [
    "123.45678.90-0",
    "12345678900",
])
def test_validate_valid_pis(valid_pis):
    """Testa PIS válidos conhecidos."""
    assert pis.validate(valid_pis), f"PIS {valid_pis} should be valid"

@pytest.mark.parametrize("invalid_pis", [
    "123.45678.90-9",
    "11111111111",
    "abcdefghijk",
    "12345678",
    "",
    "123456789012",
])
def test_validate_invalid_pis(invalid_pis):
    """Testa PIS inválidos que devem falhar."""
    assert not pis.validate(invalid_pis), f"PIS {invalid_pis} should be invalid"
