import os
import string
from collections import Counter

FILE_NAME = "employees.txt"
OUTPUT_FILE = "word_count_report.txt"


if not os.path.exists(FILE_NAME):
    print(f"{FILE_NAME} does not exist. Please enter a paragraph to create the file:")
    with open(FILE_NAME, "w") as file:
        file.write(input("Enter text: ") + "\n")

def count_word_frequency():
    with open(FILE_NAME, "r") as file:
        text = file.read().lower()


    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()

    word_counts = Counter(words)

    total_words = sum(word_counts.values())
    top_words = word_counts.most_common(5)

    print(f"Total words: {total_words}")
    print("Top 5 most common words:")
    for word, count in top_words:
        print(f"{word} - {count} times")

    # Write to output file
    with open(OUTPUT_FILE, "w") as file:
        file.write("Word Count Report\n")
        file.write(f"Total Words: {total_words}\n")
        file.write("Top 5 Words:\n")
        for word, count in top_words:
            file.write(f"{word} - {count}\n")

    print(f"Word count report saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    count_word_frequency()
