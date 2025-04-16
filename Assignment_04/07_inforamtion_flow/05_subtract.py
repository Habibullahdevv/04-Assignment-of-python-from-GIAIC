def subtract_seven(number):
    """
    Subtracts 7 from the given number and returns the result.
    """
    return number - 7

def main():
    num = int(input("Enter a number: "))
    result = subtract_seven(num)
    print(f"Result after subtracting 7: {result}")

if __name__ == '__main__':
    main()
