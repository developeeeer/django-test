from rest_framework.exceptions import APIException

class ValidationException(APIException):
    status_code = 400
    default_detail = {"detail": "データに問題があります"}
