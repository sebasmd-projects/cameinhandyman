import json
from django.core.exceptions import ImproperlyConfigured

with open("sensitive_data.json") as f:
    value = json.loads(f.read())

def get_value(value_title, values=value):
    try:
        return values[value_title]
    except:
        msg = f"The name of {value_title} doesn't exists"
        raise ImproperlyConfigured(msg)