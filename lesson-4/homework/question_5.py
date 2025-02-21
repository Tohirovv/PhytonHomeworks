password = input("Enter the password: ")
if len(password)<8:
    print("Password is too short")
if password.lower() == password:
    print("Password must contain an uppercase letter.")
if len(password)>8 and password.lower() != password:
    print("Password is strong.")