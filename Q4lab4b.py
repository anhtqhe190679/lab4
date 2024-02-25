def hash_display(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            formatted_content = '#'.join(content)
            print(formatted_content)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")

def JTOI(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            corrected_content = content.replace('J', 'I')
            print(corrected_content)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")

print("Content of matter.txt with # separating each character:")
hash_display("matter.txt")

print("Content of WORDS.TXT with 'J' replaced by 'I':")
JTOI("WORDS.TXT")
