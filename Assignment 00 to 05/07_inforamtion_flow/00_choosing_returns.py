LEGAL_AGE = 18

def check_adult(age):
    return age >= LEGAL_AGE

def main():
    user_age = int(input("Enter the person's age: "))
    print(check_adult(user_age))

if __name__ == '__main__':
    main()
