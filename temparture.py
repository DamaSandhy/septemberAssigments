choice = input("Enter your choice(C to F or F to C):")
if choice == "C to F":
    celsius = float(input("Enter the temparture in celsius:")) 
    farenheit = (celsius *9/5) +32
    print(f"The temperature in farenheit is:{farenheit}F")
elif choice == "F to C":
    farenheit = float(input("Enter the temperature in farenheit:"))
    celsius = (farenheit -32) * 5/9
    print(f" The temperature in celsius is:{celsius} C")
else:
    print("Invalid choice.please try again.")