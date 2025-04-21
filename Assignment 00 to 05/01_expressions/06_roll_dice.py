import random

def main():
 dise1 =  random.randint(1, 6)
 dise2 =  random.randint(1, 6)

 total = dise1 + dise2   


 print("Problem Statement 06-roll-dice!")
 print("Rolling the dice!!")
    
 print("Dice 1: " + str(dise1))
 print("Dice 2: " + str(dise2))

    
    
 print("The sum of the dice " + str(total))

print()




if __name__ == "__main__":
    main()
