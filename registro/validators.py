from django.core.exceptions import ValidationError

def num_validation(value):
    try:
        int(value)
    except ValueError:
        raise ValidationError('El campo debe ser de tipo numérico')