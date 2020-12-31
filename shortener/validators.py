from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

def validate_url(value):
	url_validator = URLValidator()
	reg_val = value
	if "http" in reg_val:
		new_value = reg_val
	else:
		new_value = "http://" + value

	try:
		url_validator(new_value)
	except:
		raise ValidationError("Invalid URL for this field")
	return new_value

def validate_dot_com(value):
	extensions = [".com", ".org", ".edu", 
				  ".net", ".gov", ".co", ".bet",
				  ".de", ".io", ".ca", ".me"]
	for i in extensions:
		if i in value:
			return value
	else:
		raise ValidationError("Invalid Extension")
