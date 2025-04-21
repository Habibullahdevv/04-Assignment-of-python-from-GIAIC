def main():
    print("Python Practice 04-pythagoras-theorem!")

    print("To find the pytohagoras theorem, we need to find the hypotenuse of a right triangle")
    print("The formula is a^2 + b^2 = c^2")
    AB = float(input("Enter the value of AB: "))
    AC = float(input("Enter the value of AC: "))

    bc = AB ** 2 + AC ** 2
    
    print("bc**2 =" + str(bc))
    print("The hypotenuse of the right triangle is: " + str(bc))


if __name__ == "__main__":
    main()
