def get_user_info():
    """
    Asks the user for their first name, last name, and email address, and returns them as a tuple.
    """
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    email = input("Enter your email address: ")
    return first, last, email

def main():
    user_info = get_user_info()
    print(f"Received user data: {user_info}")

if __name__ == '__main__':
    main()
