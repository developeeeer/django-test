from django.http import Http404
from rest_framework.exceptions import APIException

class DoesNotExistException(APIException):
    status_code = 404
    default_detail = {"detail": "対象のデータが見つかりません"}

