import random 
def main():

 Numberr:int = random.randint(1, 100)

 print("I am thinking of a number between 1 to 100 can you guess it?")
 Guessed_number:int = int(input("Enter a Guess: "))
 
 while Guessed_number != Numberr:
    if Guessed_number > Numberr:
        print("You are guessing too high")
    else :
        print("Your guess is very low")

    print()
    Guessed_number:int = int(input("Enter a Guess: "))

 return print(Guessed_number, "is correct") 

if __name__ == '__main__':
    main()