alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#',
    '$', '%', '^', '&', '*', '(', ')', '{', '}', '+', ' '
]
shift_number = int(len(alphabets)/5)

def encryption(text):
    encrypt_message = ""
    for char in text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position+shift_number)%len(alphabets)
            encrypt_message += alphabets[new_position]
        else:
            encrypt_message += char
    print(f"Here is the encrypted message: {encrypt_message}")

def decryption(cipher_text):
    decrypt_message = ""
    for char in cipher_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position-shift_number)%len(alphabets)
            decrypt_message += alphabets[new_position]
        else:
            decrypt_message += char
    print(f"Here is the encrypted message: {decrypt_message}")

message = input("Type your message to encrypt:\n")
decryption(message)
