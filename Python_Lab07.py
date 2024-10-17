# Lab 7 from https://github.com/THartmanOfTheRedwoods/PyLab007

# Part 1 - Building the Vigenere Square

alpha_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alpha_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def vig_alpha_list_of_lists(alphabet):
    rows = []
    for i in range(len(alphabet)):
        if i == 0:
            row = ' ' + alphabet[i:] + alphabet[:i]
            rows.append(list(row))
        row = alphabet[i] + alphabet[i:] + alphabet[:i]
        rows.append(list(row))
    return rows

def format_vigenere_sq(rows):
    for i, row in enumerate(rows):
        print(f'| { " | ".join(row) } |')
        if i == 0:
            print('|---' * len(row) + '|')

list_in_list = vig_alpha_list_of_lists(alpha_string)
# format_vigenere_sq(list_in_list)

# Part 2 - Encryption

def letter_to_index(letter, alphabet):
    letter = letter.lower()
    for i, l in enumerate(alphabet.lower()):
        if l == letter:
            return i
    return -1

def index_to_letter(alphabet, index2):
    if 0 <= index2 < len(alphabet):
        return alphabet[index2]
    return -1

# print(letter_to_index('A', alpha_string))
# print(index_to_letter(alpha_string, 23))

def vigenere_index(key_letter, plaintext_letter, alphabet):
    k_index = letter_to_index(key_letter, alphabet)
    p_index = letter_to_index(plaintext_letter, alphabet)
    vigenere_cipher = (p_index + k_index) % len(alphabet)
    return index_to_letter(alphabet, vigenere_cipher)

def encrypt_vigenere(keyword, plaintext, alphabet):
    cipher_text = []
    k_length = len(keyword)
    for i, l in enumerate(plaintext):
        cipher_text.append(vigenere_index(keyword[i % k_length], l, alphabet) if l != ' ' else l)
    return ''.join(cipher_text)

key = 'DAVINCI'
message = 'the eagle has landed'

# print(encrypt_vigenere(key, message, alpha_string + ' '))

# Part 3 - Decryption

def undo_vigenere_index(key_letter, cypher_letter, alphabet):
    k_index = letter_to_index(key_letter, alphabet)
    vigenere_cipher = letter_to_index(cypher_letter, alphabet)
    p_index = (vigenere_cipher - k_index) % len(alphabet)
    return index_to_letter(alphabet, p_index)

def decrypt_vigenere(key_word, cipher_text, alphabet):
    plain_text = []
    k_length = len(key_word)
    for i, l in enumerate(cipher_text):
        plain_text.append(undo_vigenere_index(key_word[i % k_length], l, alphabet) if l != ' ' else l)
    return ''.join(plain_text)

secret_message = 'WHZHRCOOEUPNUHOAHLRF'

# print(decrypt_vigenere(key, secret_message, alpha_string + ' '))

# Part 4 - App w/ Menu

def encrypt():
    encrypt_message = input('Enter a message you wish to encrypt:\n')
    encrypt_key = input('Enter an encryption word.\n')
    print(f'Your encrypted message is {encrypt_vigenere(encrypt_key, encrypt_message, alpha_string)}.\n')
    return encrypt_vigenere(encrypt_key, encrypt_message, alpha_string)

def decrypt():
    decrypt_message = input('Enter a message you wish decrypted:\n')
    decrypt_key = input('Enter encryption word.\n')
    print(f'Your decrypted message is {encrypt_vigenere(decrypt_key, decrypt_message, alpha_string)}.\n')
    return encrypt_vigenere(decrypt_key, decrypt_message, alpha_string)



def app_menu():
    printable_menu = ['1) Encrypt', '2) Decrypt', '3) Dump Encrypted Text', '4) Quit']
    print(printable_menu)
    user_pick = input('Choose from above menu.\n')
    if user_pick == '1':
        encrypt()
        app_menu()
    elif user_pick == '2':
        decrypt()
        app_menu()
    elif user_pick == '3':
        print(global_list)
    elif user_pick == '4':
        print('Thank you. Have a nice day.')
    else:
        print('Invalid response. Enter number for desired menu item.\n')
        app_menu()

def which():
    print(f'This is an encryption program using the Vigenere Cipher.\n')
    first_choice = input('Would you like to see what the Vigenere Cipher looks like?\n')
    if first_choice in ['yes', 'y', 'Yes', 'Y']:
        format_vigenere_sq(list_in_list)
    else:
        pass
    second_choice = input("Are you interested in decrypting or encrypting using the Vigenere Cipher?\n")
    if second_choice in ['yes','y','Yes','Y']:
        app_menu()
    else:
        print("Then why are you here?")

def main_program():
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encrypted_list = []
    menu = [
        ['1) Encrypt', encrypt],
        ['2) Decrypt', decrypt],
        '3) Dump Encrypted Text',
        '4) Quit',
        [[key, alphabet],[key, encrypted_list], [0] ],
        [1,2,3]
    ]

which()

# Bonus -

