import random

# Step 1: Generate a random two-digit lottery number
lottery_number = random.randint(10, 99)

# Step 2: Prompt the user to enter a two-digit number
user_input = input("Enter a two-digit number (e.g., 45): ")

# Ensure the user input is a two-digit number
if len(user_input) != 2 or not user_input.isdigit():
    print("Invalid input. Please enter a valid two-digit number.")
else:
    user_number = int(user_input)

    # Step 3: Determine if the user wins and calculate the award
    if user_number == lottery_number:
        award = 10000  # Exact match
    elif sorted(str(user_number)) == sorted(str(lottery_number)):
        award = 3000  # All digits match
    elif (user_number % 10 == lottery_number % 10) or (user_number // 10 == lottery_number // 10) or \
         (user_number % 10 == lottery_number // 10) or (user_number // 10 == lottery_number % 10):
        award = 1000  # One digit matches
    else:
        award = 0  # No match

    # Step 4: Display the lottery number and the result
    print(f"Lottery Number: {lottery_number}")
    if award > 0:
        print(f"Congratulations! You win ${award}.")
    else:
        print("Sorry, you didn't win this time.")

