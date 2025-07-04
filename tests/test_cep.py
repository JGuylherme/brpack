import pytest
import re
from brpack import cep
import requests

@pytest.mark.parametrize("cep_to_test", [
    "01001000",
    "23590807",
])
def test_valid_cep_and_existence(cep_to_test):
    """Test valid CEP format and that CEP exists via API."""
    assert cep.validate(cep_to_test)
    assert cep.check_cep_exists(cep_to_test), f"CEP {cep_to_test} should exist"

def test_valid_cep_format_but_nonexistent():
    """Test valid CEP format but nonexistent CEP."""
    fake_cep = "99999999"
    assert cep.validate(fake_cep)
    assert not cep.check_cep_exists(fake_cep), f"CEP {fake_cep} should NOT exist"

@pytest.mark.parametrize("invalid_cep", [
    "12345",
    "12a45-67b",
    "950100100",
    "95010A10",
    "95010 10",
    "",
    "abcdefghi",
])
def test_invalid_cep_format(invalid_cep):
    """Test invalid CEP formats rejected by validation."""
    assert not cep.validate(invalid_cep)

def test_format_valid_and_invalid():
    """Test CEP formatting function with valid and invalid inputs."""
    valid_unmasked = "01001000"
    valid_masked = "01001-000"
    assert cep.format(valid_unmasked) == "01001-000"
    assert cep.format(valid_masked) == "01001-000"

    with pytest.raises(ValueError):
        cep.format("123")
    with pytest.raises(ValueError):
        cep.format("abcdefghi")
