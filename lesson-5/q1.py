def convert_cel_to_far(celsius):
    return round(celsius * 9/5 + 32, 2)

def convert_far_to_cel(fahrenheit):
    return round((fahrenheit - 32) * 5/9, 2)

a = float(input("Enter a temperature in degrees F: "))
print(f"{a} degrees F = {convert_far_to_cel(a)} degrees C")

b = float(input("\nEnter a temperature in degrees C: "))
print(f"{b} degrees C = {convert_cel_to_far(b)} degrees F")

