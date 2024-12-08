from Szyfr import alphabet_cipher ,alphabet_cipher2
from joblib import delayed, Parallel

def encryption(file):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    words = content.split()
    encrypted_words = []
    for word in words:
        encrypted_word = ""
        for letter in word:
            if letter in alphabet_cipher:
                encrypted_word += alphabet_cipher[letter]
                print(f"Poprawiona litera: {letter}, na literę: {alphabet_cipher[letter]}")
            else:
                encrypted_word += letter
        encrypted_words.append(encrypted_word)
    encrypted_content = ' '.join(encrypted_words)
    with open("encrypted_text.txt", 'w', encoding='utf-8') as corrected_text:
        corrected_text.write(encrypted_content)
    print(f"Poprawiony plik został zapisany pod nazwą 'encrypted_text.txt'")



def decryption(file):
    reverse_cipher = {v: k for k, v in alphabet_cipher.items()}
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    decrypted_content = ""
    for letter in content:
        if letter in reverse_cipher:
            decrypted_content += reverse_cipher[letter]
            print(f"Poprawiona litera: {letter} na literę: {reverse_cipher[letter]}")
        else:
            decrypted_content += letter
    with open("decrypted_text.txt", 'w', encoding='utf-8') as corrected_text:
        corrected_text.write(decrypted_content)
    print(f"Poprawiony plik został zapisany pod nazwą 'decrypted_text.txt'")



a1 = Parallel(n_jobs=2)(delayed(encryption)("pg11.txt") for i in range(1))
a2 = Parallel(n_jobs=2)(delayed(decryption)("encrypted_text.txt") for i in range(1))

