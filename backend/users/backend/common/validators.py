from django.core.exceptions import ValidationError


def validate_user_in_text(value):
    if '{user}' not in value:
        raise ValidationError("В тексте должно присуствовать {user}")


def validate_url_in_text(value):
    if '{url}' not in value:
        raise ValidationError("В тексте должно присуствовать {url}")
