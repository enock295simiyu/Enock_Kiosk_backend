from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
from config_master import ROLE_CHOICES, NOTIFICATION_CHOICES, NOTIFICATION_EMAIL


class User(AbstractUser):
    """
    Custom user model
    """
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)  # Role of the user
    phone_number = PhoneNumberField(null=True, blank=True)  # Phone number of the user
    is_phone_verified = models.BooleanField(default=False)  # Whether the phone number is verified
    sub_domain = models.CharField(max_length=100, null=True, blank=True)  # Subdomain of the user
    timezone = models.CharField(max_length=100, null=True, blank=True)  # Timezone of the user
    country = models.CharField(max_length=100, null=True, blank=True)  # Country of the user
    currency_symbol = models.CharField(max_length=100, null=True, blank=True)  # Currency symbol of the user
    notification_method = models.CharField(max_length=100, null=True, blank=True, default=NOTIFICATION_EMAIL,
                                           choices=NOTIFICATION_CHOICES)  # Notification method of the user
    enable_calendar_module = models.BooleanField(default=False)  # Whether the calendar module is enabled


class AccountsManager:
    """
    This class handles all the functionalities related to the user accounts
    """

    def get_all_users(self):
        """
        This method returns all the users in the database
        :return:
        """
        return User.objects.all()

    def get_user_by_id(self, user_id):
        """
        This method returns the user with the given id
        :param user_id: The id of the user
        :return: The user object or None if not found
        """
        users = User.objects.filter(id=user_id)
        if users:
            return users.first()
        return None
