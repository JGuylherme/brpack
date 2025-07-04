import pytest
from brpack import cpf

def test_generate_and_validate():
    """
    Generates an unmasked CPF and validates it. Should always be valid.
    """
    generated = cpf.generate()
    assert cpf.validate(generated), "Generated CPF should be valid"

def test_generate_with_mask():
    """
    Generates a masked CPF and validates it. Should be a string and valid.
    """
    masked = cpf.generate(masked=True)
    assert isinstance(masked, str), "Masked CPF should be a string"
    assert cpf.validate(masked), "Masked CPF should be valid"

def test_invalid_cpf_repeated_digits():
    """
    Tests CPFs with all identical digits, which are always invalid by rule.
    """
    for repeated in ["111.111.111-11", "00000000000", "99999999999"]:
        assert not cpf.validate(repeated), f"CPF {repeated} should be invalid"

def test_invalid_cpf_length():
    """
    Tests CPFs with incorrect lengths.
    """
    for short in ["123", "123456789", "123456789000", ""]:
        assert not cpf.validate(short), f"CPF {short} should be invalid"

def test_invalid_cpf_non_numeric():
    """
    Tests CPFs containing non-numeric or malformed input.
    """
    cpfs = [
        "abc.def.ghi-jk",
        "123.456.78A-99",
        "###.###.###-##",
        "invalid CPF"
    ]
    for cpf_str in cpfs:
        assert not cpf.validate(cpf_str), f"CPF {cpf_str} should be invalid"
