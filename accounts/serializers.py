from rest_framework import serializers

from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'first_name', 'last_name', 'role', 'phone_number', 'email', 'is_staff', 'phone_number',
            'is_phone_verified', 'sub_domain', 'timezone', 'country', 'currency_symbol', 'notification_method',
            'enable_calendar_module')
