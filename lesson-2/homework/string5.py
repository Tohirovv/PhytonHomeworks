s = input("Enter a string: ").lower()
vowels = "aeiou"
vowel_count = sum(1 for c in s if c in vowels)
consonant_count = sum(1 for c in s if c.isalpha() and c not in vowels)
print(f"Vowels: {vowel_count}, Consonants: {consonant_count}")