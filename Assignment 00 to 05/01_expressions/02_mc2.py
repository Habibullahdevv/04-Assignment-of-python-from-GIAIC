def main():
 print("Python practice E=m*c**2");

 mass =  float(input("Enter the mass(m) in kg : "));
 speed_of_light =  299792458;
 energy = mass * speed_of_light**2;

 print("Mass is : " + str(mass) + " kg");
 print("Speed of light is : " + str(speed_of_light) + " m/s");
 print("Energy is : " + str(energy) + " Joules");



if __name__ == "__main__":
    main()
