import random
random_number= random.randint(0, 5)
user_input_number = int(input('Enter your number between 0- 5: '))
if random_number==user_input_number:
    print("your guess is right")
elif random_number>user_input_number:
    print("your input is less than the random number")
else:
     print("your input is greater than the random number")


    