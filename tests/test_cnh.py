import pytest
from brpack import cnh

def test_generate_unmasked():
    """
    Testa geração de CNH não formatada.
    """
    cnh_number = cnh.generate(masked=False)
    assert isinstance(cnh_number, str)
    assert len(cnh_number) == 11
    assert cnh.validate(cnh_number), f"Generated CNH {cnh_number} should be valid"

def test_generate_masked():
    """
    Testa geração de CNH formatada.
    """
    cnh_number = cnh.generate(masked=True)
    assert isinstance(cnh_number, str)
    assert len(cnh_number) == 12
    assert cnh.validate(cnh_number), f"Generated masked CNH {cnh_number} should be valid"

def test_validate_valid_generated():
    """
    Testa CNHs geradas dinamicamente que devem ser válidas.
    """
    for _ in range(5):
        valid_cnh = cnh.generate()
        assert cnh.validate(valid_cnh), f"Generated CNH {valid_cnh} should be valid"

@pytest.mark.parametrize("invalid_cnh", [
    "11111111111",
    "12345678901",
    "abcdefghijk",
    "12345678",
    "",
    "123456789012",
])
def test_validate_invalid_cnhs(invalid_cnh):
    """
    Testa CNHs inválidas que devem falhar na validação.
    """
    assert not cnh.validate(invalid_cnh), f"CNH {invalid_cnh} should be invalid"
