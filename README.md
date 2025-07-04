# brpack

**brpack** is a Python library for the generation, validation, and formatting of common Brazilian data used in documents, systems, and forms. It includes tools for working with CPF, CNPJ, RG, CNH, CEP, phone numbers, vehicle plates, and more.

It also offers integration with the [ViaCEP API](https://viacep.com.br) to verify the existence of a given CEP in real time.

---

## Features

- Generate and validate CPF (Cadastro de Pessoas Físicas)
- Generate and validate CNPJ (Cadastro Nacional da Pessoa Jurídica)
- Generate and validate RG (Registro Geral)
- Generate and validate CNH (Carteira Nacional de Habilitação)
- Generate, validate, and format CEP (Código de Endereçamento Postal)
- Check existence of CEP via ViaCEP API
- Generate and validate Título de Eleitor
- Generate and validate PIS and NIS numbers
- Generate and validate Brazilian phone numbers (mobile and landline)
- Generate and validate vehicle license plates (Mercosul and legacy formats)

---

## Installation

Install the library via pip:

```bash
pip install brpack
```

Note: This package requires Python 3.12 or higher.

## Example Usage

```
from brpack import cnpj

cnpj_number = cnpj.generate(masked=True)
print("CNPJ:", cnpj_number, "is valid?", cnpj.validate(cnpj_number))
```

| Module   | Function                   | Parameters                                    | Return | Description                                                               |
| -------- | -------------------------- | --------------------------------------------- | ------ | ------------------------------------------------------------------------- |
| `cnh`    | `generate(masked)`         | `masked: bool = False`                        | `str`  | Generates a valid CNH number                                              |
|          | `validate(cnh)`            | `cnh: str`                                    | `bool` | Validates a CNH number                                                    |
| `cnpj`   | `generate(masked)`         | `masked: bool = False`                        | `str`  | Generates a valid CNPJ number                                             |
|          | `validate(cnpj)`           | `cnpj: str`                                   | `bool` | Validates a CNPJ number                                                   |
| `cep`    | `validate(cep)`            | `cep: str`                                    | `bool` | Checks if CEP is 8 digits                                                 |
|          | `format(cep)`              | `cep: str`                                    | `str`  | Formats CEP as `12345-678`                                                |
|          | `check_cep_exists(cep)`    | `cep: str`                                    | `bool` | Checks CEP existence via ViaCEP API                                       |
| `nis`    | `generate(masked)`         | `masked: bool = False`                        | `str`  | Generates a valid NIS number                                              |
|          | `validate(nis)`            | `nis: str`                                    | `bool` | Validates a NIS number                                                    |
| `pis`    | `generate(masked)`         | `masked: bool = False`                        | `str`  | Generates a valid PIS number                                              |
|          | `validate(pis)`            | `pis: str`                                    | `bool` | Validates a PIS number                                                    |
| `rg`     | `generate(masked)`         | `masked: bool = False`                        | `str`  | Generates a random RG number (masked or not)                              |
|          | `validate(rg)`             | `rg: str`                                     | `bool` | Validates RG format (masked or unmasked, with optional 'X' as last digit) |
| `titulo` | `generate(masked)`         | `masked: bool = False`                        | `str`  | Generates a valid voter registration number                               |
|          | `validate(titulo)`         | `titulo: str`                                 | `bool` | Validates a Título de Eleitor (12-digit voter registration number)        |
| `phone`  | `generate(mobile, masked)` | `mobile: bool = True`, `masked: bool = False` | `str`  | Generates Brazilian mobile or landline number                             |
|          | `validate(phone)`          | `phone: str`                                  | `bool` | Validates phone number format (masked/unmasked)                           |
| `placa`  | `generate(mercosul)`       | `mercosul: bool = False`                      | `str`  | Generates vehicle plate (old or Mercosul format)                          |
|          | `validate(plate)`          | `plate: str`                                  | `bool` | Validates vehicle plate format (ABC-1234 or ABC1D23)                      |

## Masked Parameter

The `masked` parameter controls whether the output includes standard formatting:

- `masked=True`: returns data **with formatting**, for example:
  `123.456.789-00`, `(11) 91234-5678`, `12.345.678/0001-95`

- `masked=False` (default): returns data **with plain digits only**, for example:
  `12345678900`, `11912345678`, `12345678000195`

## Development
To run tests locally, install the development dependencies:

```bash
pip install -e .[dev]
pytest
```

## License
This project is licensed under the MIT License. See LICENSE for more information.