

min_req_height = 50  

def check_ride_eligibility(user_height):
    return user_height >= min_req_height

def main():
    while True:
        height_input = input("Enter your height (press Enter to quit): ")
        
        if height_input == "":
            print("Thanks for using the Ride Checker! Goodbye!")
            break

        if not height_input.isdigit():
            print("Oops! Please enter a valid number.")
            continue

        user_height = int(height_input)

        if check_ride_eligibility(user_height):
            print("You meet the height requirement")
        else:
            print("You're not quite tall enough yet.")

if __name__ == '__main__':
    main()
