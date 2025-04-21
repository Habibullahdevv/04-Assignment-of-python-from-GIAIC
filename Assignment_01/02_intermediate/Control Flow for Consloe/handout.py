import random;

def main():

 points: int=0

 print("Welcome to the Higher-Low game !!")
 rounds = int(input("how many would you liKe to play? :"))

 for i in range(rounds):
    print()
    print(f"Round no.**{i+1}**" )
    C_number : int= random.randint(1,100) 
    Mine_number : int= random.randint(1,100)

    print(f"Your Points:--{points}--")
    print(f"Your number is: {Mine_number}.")
    print()
    high_low = input("If you think your number is higher then mine number write: \"Higher\" and \"Lower\" for lower: ").strip().lower()
  
    if(high_low == "higher" and Mine_number > C_number) or (high_low == "lower" and Mine_number < C_number ) :
        print()
        print(f"you are right!  my number was {C_number}")
        points +=1;
    
    else:
         print(f"Wrong my number was {C_number}")
         print(f"Your Points are now:--{points}--")
 print()
 print("##GAME-OVER##")
 print()
 print(f"your total score is {points}")
 if points == rounds or points == rounds -2 :  
    print("You played well!")
 else:
    print("Not Good!")
if __name__ == "__main__":
 main();