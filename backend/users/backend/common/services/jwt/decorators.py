from common.services.jwt.exceptions import PayloadError


def validate_payload_data(func):
    required_fields = ['user_id', 'role']

    def wrapper(self, data):
        for field in required_fields:
            if field not in data:
                raise PayloadError(f"Payload must contain '{field}'")
        return func(self, data)

    return wrapper
