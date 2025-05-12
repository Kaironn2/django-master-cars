from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
)

year_validator = [
    MinValueValidator(1000, message='Ano deve ter 4 dígitos.'),
    MaxValueValidator(9999, message='Ano deve ter 4 dígitos.'),
]
