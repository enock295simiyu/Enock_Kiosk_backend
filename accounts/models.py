from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
from config_master import ROLE_CHOICES


class User(AbstractUser):
    """
    Custom user model
    """
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)  # Role of the user
    phone_number = PhoneNumberField(null=True, blank=True)  # Phone number of the user
    is_phone_verified = models.BooleanField(default=False)  # Whether the phone number is verified

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
