from rest_framework import serializers

class RequiredValidator:
    def __init__(self):
        pass

    def __call__(self, value):
        if value == None:
            message = '必須項目です'
            raise serializers.ValidationError(message)