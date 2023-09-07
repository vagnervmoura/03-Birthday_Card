import datetime
from datetime import datetime

min = 2
med = 3
max = 4

input_name_sender = input("What is the name of the sender's? ")
input_name_birth = input("What is the name of birthday person? ")
input_year_birth = None
age = None

while age is None:
    try:
        input_year_birth = abs(int(input("What is the year of the birthday person born? "))) # "ABS" will check if the input was a negative number and if yes, convert to a positive
        lim = len(str(input_year_birth))   
        print("lim", lim) 
          
        if lim > max or lim < min or lim == 3:
            print("Sorry, but you have input a wrong date, please let's try again with an valid date with 2 or 4 digits of the year.")       
        else:
            print("Primeiro if")
            year = datetime.now().year
            new_year = str(year)
            half_year = int(new_year[2:4]) # To use in case the Year of the Input have 2 digits.

            if lim == 2:
                age = half_year - input_year_birth + 100
            else: 
                age = year - input_year_birth
    except: 
        print("Sorry, but you have input a wrong date, please let's try again with an valid date with 2 or 4 digits of the year.")

print("Hi, {} let's write here a short personalized message to {}?".format(input_name_sender, input_name_birth))
message = input()

print("\n\n\n\n{0}, let's celebrate your {1} years of awesomeness!\n\n"
    "Wishing you a day filled with joy and laughter as you turn {1}!\n"
    "{2}\n"
    "\n\nWith love and best wishes,\n"
    "{3}".format(input_name_birth, age, message, input_name_sender))