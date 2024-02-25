def count_uppercase_characters(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            count = 0
            for char in content:
                if char.isupper():
                    count += 1
            return count
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")

def count_specific_words(filename, *words):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            count = 0
            for word in words:
                count += content.count(word)
            return count
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")

filename = "article.txt"
uppercase_count = count_uppercase_characters(filename)
if uppercase_count is not None:
    print(f"Total number of uppercase characters in {filename}: {uppercase_count}")

word_count_this = count_specific_words(filename, "this")
word_count_these = count_specific_words(filename, "these")

if word_count_this is not None and word_count_these is not None:
    print(f"Number of occurrences of 'this' in {filename}: {word_count_this}")
    print(f"Number of occurrences of 'these' in {filename}: {word_count_these}")

