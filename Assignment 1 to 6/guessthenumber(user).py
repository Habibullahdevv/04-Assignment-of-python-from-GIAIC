import random
low: int= 1
high: int= 10

feedback = '';

print("think of a number and i will try to guess it!")
while feedback !='c':
    
    guess = random.randint(1,10)
    

    print(f"is it {guess}?")
    high_low = input("ok so write \'H\' if it is high or \'L\' for low and for correct guess write \'C\' if it is correct! ").strip().lower()

    if high_low == "h":
        high = guess - 1
    elif high_low == "l":
        low = guess + 1
    elif high_low == "c":
        print(f"Finally, I guessed your number {guess} correctly")
        feedback == "c"
        break
    else:
        print("Invalid input Please enter 'h' (too high) 'l' (too low) or 'c' (correct).")



