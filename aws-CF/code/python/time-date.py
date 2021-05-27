# working with time-date module
import datetime
from datetime import *

user_input = input("enter goal with future date ex: learn python:23.07.2021\n")
input_list = user_input.split(":")
goal = input_list[0]
deadline = input_list[1]
deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.today()
# calculation of remaining date

time_remaining = deadline_date - today_date
hours_till = int(time_remaining.seconds /60 / 60)
print(f"days remaining for your {goal} is {hours_till} hours ")











