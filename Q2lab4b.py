def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")

def display_words_less_than_4_characters(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    if len(word) < 4:
                        print(word)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")

filename = "story.txt"
word_count = count_words_in_file(filename)
if word_count:
    print(f"Total number of words in {filename}: {word_count}")

print(f"Words less than 4 characters in {filename}:")
display_words_less_than_4_characters(filename)
