def main():
    print("Welcome to the Planetary Weight Calculator!")
    
    weight_earth = float(input("Enter your weight on Earth: "))
    
    gravity_diff = {
        "mercury": 0.376,
        "venus": 0.889,
        "mars": 0.378,
        "jupiter": 2.36,
        "saturn": 1.081,
        "uranus": 0.815,
        "neptune": 1.14
    }
    
    planet = input("Enter a planet: ").strip().lower()
    
    if planet in gravity_diff:

        planet_weight = round(earth_weight * gravity_diff[planet], 2)
        print(f"The equivalent weight on {planet}: {planet_weight}")
    else:
        print("Invalid planet name. Please enter a valid planet name from the solar system.")
    

if __name__ == "__main__":
    main()