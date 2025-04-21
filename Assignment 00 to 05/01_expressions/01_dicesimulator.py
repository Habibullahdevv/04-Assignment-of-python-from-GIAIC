import random
def diceRoll():
    print("Dice Simultor game!")


    dice1 =  random.randint(1, 6)
    dice2 =  random.randint(1, 6)


    print("Dice 1: " + str(dice1))
    print("Dice 2: " + str(dice2))
    print("Sum of dice:" + str(dice1 + dice2))

def main(): 
    
    print("rolling the dice three times")

    diceRoll();
    diceRoll();
    diceRoll();



if __name__ == "__main__":
    main()
