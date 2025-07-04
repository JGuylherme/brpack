import pytest
from brpack import cnpj

def test_generate_and_validate():
    """
    Generates an unmasked CNPJ and validates it. Should always be valid.
    """
    generated = cnpj.generate()
    assert cnpj.validate(generated), "Generated CNPJ should be valid"

def test_generate_with_mask():
    """
    Generates a masked CNPJ and validates it. Should be a string and valid.
    """
    masked = cnpj.generate(masked=True)
    assert isinstance(masked, str), "Masked CNPJ should be a string"
    assert cnpj.validate(masked), "Masked CNPJ should be valid"

def test_invalid_cnpj_repeated_digits():
    """
    Tests CNPJs with all identical digits, which are always invalid by rule.
    """
    for repeated in [
        "11.111.111/1111-11",
        "00000000000000",
        "99999999999999"
    ]:
        assert not cnpj.validate(repeated), f"CNPJ {repeated} should be invalid"

def test_invalid_cnpj_length():
    """
    Tests CNPJs with incorrect lengths.
    """
    for invalid_len in ["123", "123456789", "123456789000000", ""]:
        assert not cnpj.validate(invalid_len), f"CNPJ {invalid_len} should be invalid"

def test_invalid_cnpj_non_numeric():
    """
    Tests CNPJs containing non-numeric or malformed input.
    """
    cnps = [
        "ab.cd.efgh/ijkl-mn",
        "12.345.678/9012-3A",
        "##.###.###/####-##",
        "invalid CNPJ"
    ]
    for cnpj_str in cnps:
        assert not cnpj.validate(cnpj_str), f"CNPJ {cnpj_str} should be invalid"
