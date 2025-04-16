def main():
    print("Problem Statement 05-remainder-division!")

    print("Find the result of the division with a remainder.")
  
    inpput_dividend = float(input("Enter the dividend: "))
    inpput_divisor = float(input("Enter the divisor: "))

    quotient = inpput_dividend // inpput_divisor  #for the reminder
    remainder = inpput_dividend % inpput_divisor  #for the decimal
    
    print("The quotient is: " + str(quotient) + " and the remainder is: " + str(remainder))




if __name__ == "__main__":
    main()
