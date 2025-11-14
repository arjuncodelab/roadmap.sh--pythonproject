import random
import time

levels = ["easy", "medium", "hard"]
chances = {"easy": 10, "medium": 5, "hard": 3}

print(
    """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
******************************************
"""
)

while True:
    try:
        start = time.time()
        level = input("Enter Your Choice: ").lower().strip()
        if level not in levels:
            print('Please Enter "Easy","Medium" or "Hard"')
        else:
            print(
                f"""Great! You have selected the {level} difficulty level.
Let's start the game!
You have {chances[level]} chances
"""
            )
            ans = random.randint(1, 100)
            attempt = 0
            break
    except ValueError:
        continue
while True:
    try:
        guess = int(input("Enter Your Guess: "))
        if guess <= 0 or guess > 100:
            print("Value is between 1 - 100")
            attempt += 1
            continue
        elif guess > ans:
            attempt += 1
            print(f"Incorrect! The number is smaller than {guess}. Try again!")
        elif guess < ans:
            print(f"Incorrect! The number is bigger than {guess}. Try again!")
            attempt += 1
        elif guess == ans:
            timer = time.time() - start
            print(
                f"""
Congratulations! You guessed the correct number in {attempt} attempts.
Time Taken: {timer:.2f}
                """
            )
            break

        if attempt == chances[level]:
            timer = time.time() - start
            print(
                f"""
Oh, you've finished your all Chances.
Correct Answer is {ans}.
Time Taken: {timer:.2f}
Thanks For Playing.
"""
            )
            break
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 100.")
        continue
