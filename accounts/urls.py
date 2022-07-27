from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from accounts.views import UserList, UserDetail

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('users/', UserList.as_view(), name='user_list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user_detail'),
]