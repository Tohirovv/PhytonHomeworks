s = input("Enter a string: ")
has_digit = any(c.isdigit() for c in s)
if has_digit:
    print("Contains digits")
else:
    print("No digits")