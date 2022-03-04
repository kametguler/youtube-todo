from rest_framework.serializers import ModelSerializer
from .models import TodoModel


class TodoSerializer(ModelSerializer):
    class Meta:
        model = TodoModel
        fields = "__all__"
        # fields = ("name", "created_at", "updated_at", "is_done")
