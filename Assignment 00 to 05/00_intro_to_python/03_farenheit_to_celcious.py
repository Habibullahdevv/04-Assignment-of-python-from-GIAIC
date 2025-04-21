def main():

 while True:

   try:
    print("Welcome to the farenheit to celcious converter");
    farenheit = float(input("Enter the temperature in farenheit: "));
    break;
   except:
    print("Please enter a valid number");
 
 while True:
    try: 
        celcious = (farenheit - 32) * 5.0/9.0;
        
        
    except:
     print("Re-enter values")

    print("Temperature:", farenheit ," = ", celcious,"C");
    break;
if __name__ == "__main__":
    main()
