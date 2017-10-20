from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

def validate_url(value):
    url_validator = URLValidator()
    value_1_invalid = False
    value_2_invalid = False
    try:
        url_validator(value)
    except Exception as e:
        value_1_invalid = True
    
    value_2 = "http://" + value

    try:
        url_validator(value_2)
    except Exception as e:
        valid_2_invalid = True

    if value_1_invalid==True and value_2_invalid==True:     
        raise ValidationError("Invalid URL for this field")
    return value