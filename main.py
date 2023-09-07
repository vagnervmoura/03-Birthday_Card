import datetime
from datetime import datetime

input_name_sender = input("What is the name of the sender's? ")
input_name_birth = input("What is the name of birthday person? ")
input_year_birth = int(input("What is the year of the birthday person born? "))
print("Hi, {} let's write here a short personalized message to {}?".format(input_name_sender, input_name_birth))
message = input()

year = datetime.now().year

age = year - input_year_birth

print("\n\n\n\n{0}, let's celebrate your {1} years of awesomeness!\n\n"
    "Wishing you a day filled with joy and laughter as you turn {1}!\n"
    "{2}\n"
    "\n\nWith love and best wishes,\n"
    "{3}".format(input_name_birth, age, message, input_name_sender))
