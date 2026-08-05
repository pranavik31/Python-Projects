import random
generated_number = random.randint(1,100)
number_of_attempts = 0
print("Welcome to the game")
difficulty_level = input("enter difficulty level as easy or hard for number of attempts 10,5 respectively:").lower()

if difficulty_level == "easy":
    number_of_attempts = 10
elif difficulty_level == "hard" :
    number_of_attempts = 5
else:
    print("Invalid input")

while number_of_attempts != 0:
    player_input = int(input("enter the number: "))
    if player_input == generated_number:
        print("Congratulations!\nYou guessed the number correctly.")
        break
    elif player_input > generated_number:
        print("Entered number is greater than generated number. Guess a number which is lower than your previous input number.")
        number_of_attempts -=1
    else:
        print("Entered number is lower than generated number. Guess a number which is greater than your previous input number.")
        number_of_attempts -=1
    print(f"you have {number_of_attempts} attempts left")

if number_of_attempts == 0:
        print("your number of attempts are completed")
        print(f"Generated Number : {generated_number}")

