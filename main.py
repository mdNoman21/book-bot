def main():
    path = "./books/frankenstein.txt"
    text = get_text(path)
    words_count = get_words_count(text)
    chars_dict = get_chars_dict(text)
    print(f"{words_count} words found in the document")
    print_report(chars_dict)
    return text

def print_report(chars_dict):
    chars_list = list(chars_dict)
    chars_list.sort()
    for char in chars_list:
        count = chars_dict[char]
        print(f"The {char} was found {count} times")
def get_text(book_path):
    with open(book_path) as f:
        return f.read()
        

def get_words_count(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered_char = c.lower()
        if c >= 'a' and c <= 'z':
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1
    return chars

    

main()