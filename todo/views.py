from urllib import request
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from todo.models import ToDo
from rest_framework import serializers, validators
from validation import MaxLengthValidator

class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(validators=[MaxLengthValidator(20)], error_messages={"required": "必須項目です"})
    detail = serializers.CharField(validators=[MaxLengthValidator(20)], error_messages={"required": "必須項目です"})

class ListTodo(APIView):
    def get(self, request, format=None):
        todo_qs = ToDo.objects.all()
        serializer = TodoSerializer(todo_qs, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = TodoSerializer(data = request.data)
        if serializer.is_valid():
            print()
        else:
            print(serializer.errors)
        return Response("OK")