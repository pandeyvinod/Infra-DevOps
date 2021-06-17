# class object

import pyclass
import message
user1 = pyclass.User("vinod", "vinod@.com", "vinod", "DevOps Engineer")
user1.get_user_info()

user2 = pyclass.User("albert", "albert.com", "albertpwd", "scientist")
user2.get_user_info()

user3 = pyclass.User("mail.com", "mail", "mail-pwd", "mail-work")
user3.get_user_info()

user_message = message.Post("author message", user1.user_name)
user_message.get_post_message()

albert_user = message.Post("I am albert User", user2.user_name)
albert_user.get_post_message()










