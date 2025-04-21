"""
Program: Shorten a List
-----------------------
This program removes elements from the end of a list until the list
has at most MAX_LENGTH items.
"""

MAX_LENGTH = 3  # The maximum allowed length of the list

def shorten(lst):
    while len(lst) > MAX_LENGTH:  # Check if the list is longer than MAX_LENGTH
        removed_item = lst.pop()  
        print(f"Removed: {removed_item}")  

def main():
    
    user_list = []
    print("Enter items for the list (press Enter to finish):")
    while (item := input("Enter items: ")) != "":
        user_list.append(item)
    
    print("\nOriginal List:", user_list)  
    shorten(user_list)  
    print("Shortened List:", user_list)  

if __name__ == '__main__':
    main()
if __name__ == '__main__':
    main()