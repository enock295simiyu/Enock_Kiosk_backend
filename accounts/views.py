# Create your views here.
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from accounts.accounts_handler import AccountsHandler
from accounts.forms import UserCreationForm
from accounts.permissions import UserPermissions
from accounts.serializers import UserSerializer
from core.schema_genarator import CreateSchema, ListSchema


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
    permission_classes = [UserPermissions, IsAuthenticated]
    schema = CreateSchema(UserCreationForm()).create_schema()

    def post(self, request):
        """
        This API endpoint creates a new user.
        :param request:
        :return:
        """
        form = UserCreationForm(request.data)
        if form.is_valid():
            form.save()
            return Response(form.data, status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(ViewSet):
    permission_classes = [UserPermissions, IsAuthenticated]
    schemas = {
        'create': CreateSchema(UserCreationForm()).create_schema(),
        'list': ListSchema(parameters=[]).create_schema(),
        'retrieve': ListSchema(
            parameters=[{'name': 'id', 'help_text': 'A unique integer value identifying this user.'}]).create_schema(),
    }
    serializer_class = UserSerializer
    queryset = AccountsHandler().get_all_users()

    def list(self, request):
        """
        This API endpoint lists all users.
        :param request: The request object
        :return: A list of users
        """
        self.schema = ListSchema(parameters=[]).create_schema()
        serializer = UserSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        This API endpoint retrieves a user by id.
        :param request:
        :param pk:
        :return:
        """
        item = AccountsHandler().get_user_by_id(pk)
        if not item:
            return Response({'message', 'No user matched the ID'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(item)
        return Response(serializer.data)

    def create(self, request):
        """
        This API endpoint creates a user
        :param request:
        :return:
        """
        form = UserCreationForm(request.data)
        if form.is_valid():
            form.save()
            return Response(form.data, status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        pass
