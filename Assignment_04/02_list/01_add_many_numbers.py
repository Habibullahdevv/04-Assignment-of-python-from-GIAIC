def addNumbers(numbers):
    
    total = 0
    for number in numbers:
        total += number
    return total

def main():
    numbers:list = [1,2,3,4,5,];
    sum_of_numbers = addNumbers(numbers)
    print(sum_of_numbers)

main()
