from rest_framework import serializers
from django.contrib.auth.models import User
import uuid


class UserSerializer(serializers.ModelSerializer):
    # id = serializers.UUIDField(default=uuid.uuid4(), read_only=True)
    email = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email']

    # def create(self, validated_data):
        # validated_data['id'] = uuid.uuid4()
        # return super().create(validated_data)

    def get_email(self, obj):
        return obj.email if obj.email else "No email provided"
