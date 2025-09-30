import random

print("🎲 Welcome to the Guess the Number game!")
print("The computer picked a number between 1 and 100. Try to guess it!\n")

# random number
number = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Enter your guess: ")
    
    if not guess.isdigit():
        print("⚠️ That's not a number! Try again.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < number:
        print("📉 Too low!")
    elif guess > number:
        print("📈 Too high!")
    else:
        print(f"✅ Congratulations! You guessed the number {number} in {attempts} tries.")
        break

