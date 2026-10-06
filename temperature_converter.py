print("Temperature Converter")

celsius = float(input("Enter temperature in Celsius: "))


fahrenheit = (celsius * 9/5) + 32

print("Fahrenheit:", fahrenheit)

if choice.upper() == "C":
    celsius = float(input("Enter Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("Fahrenheit:", round(fahrenheit, 2))

elif choice.upper() == "F":
    fahrenheit = float(input("Enter Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print("Celsius:", round(celsius, 2))

