import random

def start_game():
    print("--- Number Guessing Game ---")
    print("I am thinking of a number between 1 and 100.")
    secret_number = random.randint(1, 100)
    attempts = 0
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Correct! You found it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    start_game()
