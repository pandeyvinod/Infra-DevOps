"""from helper import validate_execute, user_input_message

user_var = ""  # initialize the variable with the empty string
while user_var != "exit":
    user_var = input(user_input_message)
    days_units = user_var.split(":")
    days_units_dic = {"days": days_units[0], "unit": days_units[1]}
    validate_execute(days_units_dic)"""
import os
print(os.name)
# os.mkdir("/Users/vinod/Documents/vinodOS1")
venv = os.getenv("python")
print(venv)
