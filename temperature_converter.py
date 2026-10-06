print("Temperature Converter")

choice = input("Enter C for Celsius to Fahrenheit or F for Fahrenheit to Celsius: ")

if choice.upper() == "C":
    celsius = float(input("Enter Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("Fahrenheit:", round(fahrenheit, 2))

elif choice.upper() == "F":
    fahrenheit = float(input("Enter Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print("Celsius:", round(celsius, 2))

print("Thank you for using Temperature Converter!")
print("Goodbye!")