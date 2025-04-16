def main():

    curr_value = int(input("Enter a number: "))
    
    # Double the value and print until the value is 100 or greater
    while curr_value < 100:
        curr_value *= 2
        print(curr_value, end=" ")  
    
      


if __name__ == '__main__':
    main()