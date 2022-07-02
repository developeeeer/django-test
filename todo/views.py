from rest_framework.views import APIView
from rest_framework.response import Response
from todo.models import ToDo
from rest_framework import serializers, status
from util.exceptions import ValidationException, DoesNotExistException
from util.messages import ErrorMessage

class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(error_messages=ErrorMessage(field_name="名前", max_length=20).get_error_messages(), max_length=20, allow_blank=False, required=True)
    detail = serializers.CharField(error_messages=ErrorMessage(field_name="詳細", max_length=20).get_error_messages(), max_length=20, allow_blank=False, required=True)

    def create(self) -> ToDo:
        return ToDo.objects.create(**self.validated_data)

    def update(self, todo_id: int) -> ToDo:
        todo: ToDo =ToDo.objects.get_or_exception(pk=todo_id)
        todo.name = self.validated_data["name"]
        todo.detail = self.validated_data["detail"]
        todo.save()
        return todo

    def delete(self, todo_id):
        todo: ToDo = ToDo.objects.get_or_exception(pk=todo_id)
        todo.delete()


class ListCreateTodo(APIView):
    def get(self, request, format=None):
        todo_qs = ToDo.objects.all()
        serializer = TodoSerializer(todo_qs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TodoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.create()
            return Response(
                status=status.HTTP_201_CREATED,
                data={
                    "status_code": 201,
                    "data": serializer.data
                }
            )
        else:
            raise ValidationException({"detail": serializer.errors})

class UpdateDeleteTodo(APIView):
    def get(self, request, todo_id):
        todo_find_by_id_qs = ToDo.objects.get_or_exception(pk=todo_id)
        serializer = TodoSerializer(todo_find_by_id_qs, many=False)
        return Response(
            status=status.HTTP_200_OK,
            data={
                "status_code": 200,
                "data": serializer.data
            })

    def put(self, request, todo_id):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update(todo_id=todo_id)
            return Response(
                status=status.HTTP_200_OK,
                data={
                    "status_code": 200,
                    "data": serializer.data
                })
        else:
            raise ValidationException({"detail": serializer.errors})

    def delete(self, request, todo_id):
        TodoSerializer().delete(todo_id=todo_id)
        return Response(
            status=status.HTTP_204_NO_CONTENT,
            data={
                "status_code": 204,
            }
        )