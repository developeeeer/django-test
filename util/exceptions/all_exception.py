from rest_framework.exceptions import APIException

class AllException(APIException):
    status_code = 400
    default_detail = {"detail": "通信に失敗しました"}
    message = "不正なリクエストです"
