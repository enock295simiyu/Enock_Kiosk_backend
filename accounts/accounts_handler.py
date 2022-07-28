from accounts.models import AccountsManager


class AccountsHandler:
    """
    This class calls the methods in the model manager
    """

    def __init__(self):
        self.accounts_manager = AccountsManager()

    def get_all_users(self):
        """
        This method returns all the users in the database
        :return:
        """
        return self.accounts_manager.get_all_users()

    def get_user_by_id(self, user_id):
        """
        This method returns the user with the given id
        :param user_id: The id of the user
        :return: The user object or None if not found
        """
        return self.accounts_manager.get_user_by_id(user_id)
