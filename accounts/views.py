# Create your views here.
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.accounts_handler import AccountsHandler
from accounts.serializers import UserSerializer


class UserList(generics.ListAPIView):
    """
    This API endpoint allows you to list all users.
    """
    permission_classes = (IsAuthenticated,)
    queryset = AccountsHandler().get_all_users()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """
    This API endpoint allows you to retrieve a user by id.
    """
    permission_classes = (IsAuthenticated,)
    queryset = AccountsHandler().get_all_users()
    serializer_class = UserSerializer


class CreateUserView(APIView):
    def post(self, request):
        """
        This API endpoint creates a new user.
        :param request:
        :return:
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
