

import random  

def main():
    for _ in range(10):  # Loop 10 times
        number = random.randint(1, 100)  # Generate a random number between 1 and 100
        print(number, end=' ')  
    print()  


if __name__ == '__main__':
    main()