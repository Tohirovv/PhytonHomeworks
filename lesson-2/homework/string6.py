s1 = input("Enter the main string: ")
s2 = input("Enter the string to search: ")

print(f"'{s2}' found in '{s1}'" if s2 in s1 else "Not found")