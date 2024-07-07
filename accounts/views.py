from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response


class UserView(APIView):
    def get(self, request, *args, **kwargs):
        '''
        User gets all
        '''
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)

        return Response(serializer.data, status.HTTP_200_OK)
