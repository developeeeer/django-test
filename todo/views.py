from email import message
from urllib import request
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from todo.models import ToDo
from rest_framework import serializers, status
from validation import MaxLengthValidator
from util import ValidationException

class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(validators=[MaxLengthValidator(20)], error_messages={"required": "必須項目です"})
    detail = serializers.CharField(validators=[MaxLengthValidator(20)], error_messages={"required": "必須項目です"})
    
    def create(self, validated_data):
        return ToDo.objects.create(**validated_data)
        

class ListTodo(APIView):
    def get(self, request, format=None):
        todo_qs = ToDo.objects.all()
        serializer = TodoSerializer(todo_qs, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = TodoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                status=status.HTTP_201_CREATED,
                data={
                    "status_code": 201,
                    "data": serializer.data
                }
            )
        else:
            raise ValidationException({"detail": serializer.errors})
            