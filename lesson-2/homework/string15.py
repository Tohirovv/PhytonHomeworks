words = input("Enter a sentence: ").split()
acronym = "".join(word[0].upper() for word in words)
print(f"Acronym: {acronym}")