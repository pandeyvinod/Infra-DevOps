# understanding the class object

class User:
    # these are basically constructor to create the method of specified object
    def __init__(self, name, email, password, title):
        self.user_name = name
        self.user_email = email
        self.user_passwd = password
        self.user_title = title

    def change_password(self, new_password):
        self.user_passwd = new_password

    def change_title(self, new_title):
        self.user_title = new_title

    def get_user_info(self):
        print(
            f"User {self.user_name} currently works as {self.user_title}. you can contact engineer at {self.user_email}")




