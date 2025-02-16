s = input("Enter a sentence: ")
start = input("Enter the start word: ")
end = input("Enter the end word: ")
if s.startswith(start) and s.endswith(end):
    print("Match")
else:
    print("No match")