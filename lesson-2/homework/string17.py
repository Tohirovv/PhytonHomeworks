s = input("Enter a string: ")
print("".join("*" if c in "aeiouAEIOU" else c for c in s))