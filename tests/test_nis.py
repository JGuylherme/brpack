import pytest
from brpack import nis

def test_generate_unmasked():
    """Testa geração de NIS não formatado."""
    number = nis.generate(masked=False)
    assert isinstance(number, str)
    assert len(number) == 11
    assert nis.validate(number), f"Generated NIS {number} should be valid"

def test_generate_masked():
    """Testa geração de NIS formatado."""
    number = nis.generate(masked=True)
    assert isinstance(number, str)
    assert len(number) == 14
    assert nis.validate(number), f"Generated masked NIS {number} should be valid"

@pytest.mark.parametrize("valid_nis", [
    "123.45678.90-0",
    "12345678900",
])
def test_validate_valid_nis(valid_nis):
    """Testa NIS válidos conhecidos."""
    assert nis.validate(valid_nis), f"NIS {valid_nis} should be valid"

@pytest.mark.parametrize("invalid_nis", [
    "123.45678.90-9",
    "11111111111",
    "abcdefghijk",
    "12345678",
    "",
    "123456789012",
])
def test_validate_invalid_nis(invalid_nis):
    """Testa NIS inválidos que devem falhar."""
    assert not nis.validate(invalid_nis), f"NIS {invalid_nis} should be invalid"
