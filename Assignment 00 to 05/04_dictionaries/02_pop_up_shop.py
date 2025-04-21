"""
Program: Fruit Shop Calculator
------------------------------
This program calculates the total cost of fruits based on user input and predefined prices.
"""

def main():

    fruits = {
        "apple": 10.0,
        "durian": 25.0,
        "jackfruit": 20.0,
        "kiwi": 15.0,
        "rambutan": 9.5,
        "mango": 8.0
    }

    total = 0

    for fruit in fruits:
     quantity = int(input(f"How many ({fruit}) do you want?: "))
     total += quantity * fruits[fruit]

    print(f"\nYour total is ${total:.2f}")


if __name__ == "__main__":
    main()
