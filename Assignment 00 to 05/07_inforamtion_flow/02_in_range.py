def is_in_range(num, start, end):
    """
    Returns True if num is between start and end, inclusive.
    Assumes end is greater than start.
    """
    return start <= num <= end

def main():
    number = int(input("Enter a number: "))
    lower = int(input("Enter the lower limit: "))
    upper = int(input("Enter the upper limit: "))
    
    if is_in_range(number, lower, upper):
        print(f"{number} is within the range {lower} to {upper}.")
    else:
        print(f"{number} is outside the range {lower} to {upper}.")

if __name__ == '__main__':
    main()
