from rest_framework.serializers import ModelSerializer
from .models import TodoList


class TodoListSerializer(ModelSerializer):
    class Meta:
        model = TodoList
        fields = "__all__"

