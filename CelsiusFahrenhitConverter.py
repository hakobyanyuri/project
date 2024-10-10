choice = input("Select conversion type:\n1: Celsius to Fahrenheit\n2: Fahrenheit to Celsius\n_ ")
if choice == "1":
    c = int(input("Enter the temperature in degrees Celsius:"))
    f = (c * 9/5) + 32
    print(c, "°C --->", f, "°F")
elif choice == "2":
    f = int(input("Enter temperature in degrees Fahrenheit:"))
    c = (f - 32) * 5/9
    print(f, "°F --->", c, "°C")
else:
    print("Incorrect choice.")
