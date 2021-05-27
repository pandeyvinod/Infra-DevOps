# post class

class Post:
    def __init__(self, message, author):
        self.user_message = message
        self.user_author = author

    def get_post_message(self):
        print(f"{self.user_message} written by {self.user_author}")


