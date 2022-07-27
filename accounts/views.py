# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

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
