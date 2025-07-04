import pytest
from brpack import te

def test_generate_unmasked():
    """Testa geração de Título de Eleitor não formatado."""
    generated = te.generate(masked=False)
    assert isinstance(generated, str)
    assert len(generated) == 12
    assert te.validate(generated)

def test_generate_masked():
    """Testa geração de Título de Eleitor formatado."""
    generated = te.generate(masked=True)
    assert isinstance(generated, str)
    assert len(generated) == 14
    assert te.validate(generated)

@pytest.mark.parametrize("valid_te", [
    te.generate(masked=False) for _ in range(5)
])
def test_validate_valid_te(valid_te):
    """Testa títulos de eleitor gerados dinamicamente."""
    assert te.validate(valid_te)

@pytest.mark.parametrize("invalid_te", [
    "000000000000",
    "abcdefgh1234",
    "12345678901",
    "1234567890123",
    "123456789000",
])
def test_validate_invalid_te(invalid_te):
    """Testa títulos inválidos que devem falhar."""
    assert not te.validate(invalid_te)
