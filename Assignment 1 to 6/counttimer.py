import time

def countdown_timer(total_seconds):
    while total_seconds > 0:
        minutes, seconds_left = divmod(total_seconds, 60)
        time_format = f"\r{minutes:02}:{seconds_left:02}"
        print(time_format, end="")
        time.sleep(1)
        total_seconds -= 1

    print("\n⏰ Time's up!")

# Get input from user
user_input = int(input("Enter countdown time in seconds: "))
countdown_timer(user_input)