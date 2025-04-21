"""
    Create an empty list.
    Ask the user to input numbers and store them in a list. 
    Once they enter a blank line, break out of the loop and return the list.
"""

def main():
   
    numbers = []
    
    
    while True:
        user_input = input("Enter a number (or press Enter to finish): ")
         
        if user_input == "": 
            
            break 
        
        
        numbers.append(int(user_input))
    
   
    occurrences = {}
    
  
    for number in numbers:
        if number in occurrences:

            occurrences[number] += 1

        else:

            occurrences[number] = 1
    

    for number, count in occurrences.items():
        print(f"{number} appears {count} times.")


if __name__ == '__main__':
    main()