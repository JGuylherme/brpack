import pytest
from brpack import vehicle_plate as vp

def test_generate_old_format():
    """Testa geração de placa antiga (AAA-0000)."""
    plate = vp.generate(mercosul=False)
    assert vp.validate(plate), f"Generated plate {plate} should be valid"
    assert len(plate) == 8

def test_generate_mercosul_format():
    """Testa geração de placa Mercosul (AAA1A23)."""
    plate = vp.generate(mercosul=True)
    assert vp.validate(plate), f"Generated plate {plate} should be valid"
    assert len(plate) == 7

@pytest.mark.parametrize("valid_plate", [
    "ABC-1234",
    "XYZ1234",
    "BRA1B23",
    "JHD3C21"
])
def test_validate_valid_plates(valid_plate):
    """Testa placas válidas conhecidas."""
    assert vp.validate(valid_plate)

@pytest.mark.parametrize("invalid_plate", [
    "AB-1234",
    "ABCDE1234",
    "123-ABCD",
    "ABC123",
    "BRA12B3",
    "",
    "A1C1D23",
])
def test_validate_invalid_plates(invalid_plate):
    """Testa placas inválidas que devem falhar."""
    assert not vp.validate(invalid_plate)
