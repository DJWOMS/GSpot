from django.core.exceptions import ValidationError


class ValidateUserInText:
    @staticmethod
    def validate(value):
        if '{user}' not in value:
            raise ValidationError("В тексте должно присуствовать {user}")

    def __call__(self, instance):
        self.validate(instance)


class ValidateUrlInText:
    @staticmethod
    def validate(value):
        if '{url}' not in value:
            raise ValidationError("В тексте должно присуствовать {url}")

    def __call__(self, instance):
        self.validate(instance)


class ValidateTotpInUrl:
    @staticmethod
    def validate(value):
        if '{totp}' not in value:
            raise ValidationError("В ссылке должно присуствовать {totp}")

    def __call__(self, instance):
        self.validate(instance)
