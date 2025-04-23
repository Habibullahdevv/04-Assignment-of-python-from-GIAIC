import random

words = ["table", "chair","laptop","fan"]
attempts = 6
gussed_letters = []

to_guess = random.choice(words)

print("Welcome to hangman game!")

print("_" * len(to_guess))
while attempts > 0:

    guess = input("Make a guess :").lower()
    
    if len(guess) !=1 or not guess.isalpha():
        print("Write a single letter only!")
        continue
    if guess in gussed_letters:
        print("Alredy guessed it!")
        continue
    gussed_letters.append(guess)

    if guess in to_guess:
        print("Nice guess!")
        print(f"You have {attempts} attempts left.")

    else:
        attempts -= 1
        print(f"Wrong guess! You have {attempts} attempts left.")

    display_word = ""
    for letter in to_guess :
        if letter in gussed_letters:
            display_word += letter
        else: 
            display_word += "_"
    print(" ".join(display_word))

    if "_" not in display_word:
         print(f"Congratulations! You guessed the word '{to_guess}'.")
         break

if "_" in display_word:
    print(f"Game over! The word was '{to_guess}'.")