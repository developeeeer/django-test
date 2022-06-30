from rest_framework import serializers

class MaxLengthValidator:
    def __init__(self, max_length: int):
        self.max_length = max_length

    def __call__(self, value: str):
        if value.length > self.max_length:
            message = f'{self.max_length}文字以内にしてください'
            raise serializers.ValidationError(message)