from datetime import date
birth_year = input('Enter your year of birth: ')
today = date.today()
age= today.year - int(birth_year)
if age >= 18:
    print("Congrats. You are allowed to vote");
else:
    print("Sorry. You are too young to vote");
