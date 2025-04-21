"""
    Ask the user for names/numbers to story in a phonebook (dictionary).
    Returns the phonebook.
"""
def main():
    
    phonebook = {}

    print("Welcome to the Phonebook!")


    print("Type 'add' to add a contact, 'find' to search, 'list' to view all, or 'quit' to exit.")

    while True:
        command = input("\nEnter command: ").strip().lower()

        if command == 'add':
          
            name = input("Enter name: ").strip()
          
            number = input("Enter phone number: ").strip()
            phonebook[name] = number

            print(f"{name} was added to the phonebook.")

       
        elif command == 'find':
            name = input("Enter name to find: ").strip()
           
           
            if name in phonebook:
                print(f"{name}'s number is {phonebook[name]}")
            else:
                print(f"{name} was not found in the phonebook.")

        elif command == 'list':
          
            if phonebook:
          
                print("\nPhonebook contacts:")
                for name, number in phonebook.items():
                    print(f"{name}: {number}")
            else:
            
                print("Phonebook is empty.")

        elif command == 'quit':
           
            print("Goodbye!")
            break

        else:
            print("Unknown command. Try 'add', 'find', 'list', or 'quit'.")

if __name__ == '__main__':
    main()
