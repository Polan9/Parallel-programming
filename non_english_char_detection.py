from non_english_char_DICT import  non_english_symbols

def correction(file):
    with open(file, 'r+',encoding='utf-8') as f:
        content = f.read()
    for letter in content:
        if letter in non_english_symbols:
            content = content.replace(letter,non_english_symbols[letter])
            print(f"Poprawiona litera:{letter}")

    with open("corrected_text.txt", 'w',encoding='utf-8') as corrected_text:
        corrected_text.write(content)
        corrected_text.close()
    print(f"Poprawiony plik zostal zapisany pod nazwa corrected_text.txt")



correction("pg11.txt")