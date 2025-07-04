import pytest
from brpack import rg

def test_generate_unmasked():
    """Testa geração de RG não formatado."""
    rg_number = rg.generate(masked=False)
    assert isinstance(rg_number, str)
    assert len(rg_number) == 9
    assert rg.validate(rg_number), f"Generated unmasked RG {rg_number} should be valid"

def test_generate_masked():
    """Testa geração de RG formatado."""
    rg_number = rg.generate(masked=True)
    assert isinstance(rg_number, str)
    assert len(rg_number) == 12
    assert rg.validate(rg_number), f"Generated masked RG {rg_number} should be valid"

@pytest.mark.parametrize("valid_rg", [
    "12.345.678-9",
    "00.000.000-X",
    "987654321",
    "12345678X",
])
def test_validate_valid_rgs(valid_rg):
    """Testa RGS válidos conhecidos."""
    assert rg.validate(valid_rg), f"RG {valid_rg} should be valid"

@pytest.mark.parametrize("invalid_rg", [
    "12.345.678-",
    "12345678",
    "1234567890",
    "ABCDEFGHI",
    "12.345.67A-9",
    "1234.56789",
    "",
    "1234567X9",
])
def test_validate_invalid_rgs(invalid_rg):
    """Testa RGs inválidos que devem falhar."""
    assert not rg.validate(invalid_rg), f"RG {invalid_rg} should be invalid"
