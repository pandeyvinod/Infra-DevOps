# defining the variables
# conversion of days to units
def days_to_units(num_of_days, conversion_unit):
    """ return f"{num_of_days} days are  {num_of_days * to_seconds} {s_unit}"
    print(custom_message)"""
    if conversion_unit == "hours":
        return f"{num_of_days} have  {num_of_days * 24} {conversion_unit}"
    elif conversion_unit == "sec":
        return f"{num_of_days} have  {num_of_days * 24 * 60 * 60} {conversion_unit}"
    else:
        print("your conversion unit is not supported")


# user input for the program
# def validate_execute():
#     if user_var.isdigit():
#         user_input = int(user_var)
#         if user_input > 0:
#             calculate_days = days_to_units(user_input, "user input of the pring")
#             print(calculate_days)
#         elif user_input == 0:
#             print("you entered the 0, which is not valid")
#     else:
#         print("you entered string which is not valid input")

def validate_execute(days_units_dic):
    try:  # trying to handle error in general
        user_input_days = int(days_units_dic["days"])
        if user_input_days > 0:
            calculate_days = days_to_units(user_input_days, days_units_dic["unit"])
            print(calculate_days)
        elif user_input_days == 0:
            print("you entered the 0, which is not valid")
        else:
            print("you entered the negative number which is not valid")
    except ValueError:
        print("you entered string which is not valid input")


user_input_message = "Hey user, enter the num of days and conversion unit like 20:hours \n"
