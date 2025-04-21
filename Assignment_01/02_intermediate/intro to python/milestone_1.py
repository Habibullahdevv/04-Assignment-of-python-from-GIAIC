def main():
    print("Welcome to the Mars Weight Calculator!")
    weight_on_Earth = float(input("Enter your weight on Earth: "))
    
    # Mars gravity constant
    gravity_mars = 0.378
    
    # Calculate weight on Mars
    weight_on_mars = round(weight_on_Earth * gravity_mars, 2)
    
    print(f"The equivalent weight on Mars: {weight_on_mars}")


if __name__ == "__main__":
    main()