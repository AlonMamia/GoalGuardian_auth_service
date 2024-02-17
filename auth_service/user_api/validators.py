import re

from django.core.exceptions import ValidationError


def validate_user_register(clean_data):
    if not re.match(r'^[\w.@+-]+$', clean_data['username']):
        raise ValidationError(
            'Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters.')
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', clean_data['email']):
        raise ValidationError('Enter a valid email address.')

    if len(clean_data['password']) < 8:
        raise ValidationError('Password must be at least 8 characters long.')

    return clean_data


def validate_user_login(clean_data):
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', clean_data['email']):
        raise ValidationError('Enter a valid email address.')

    if len(clean_data['password']) < 8:
        raise ValidationError('Password must be at least 8 characters long.')

    return clean_data
