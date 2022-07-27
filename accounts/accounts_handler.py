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
