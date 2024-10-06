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
    encrypted_message = ""
    for char in text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position+shift_number)%len(alphabets)
            encrypted_message += alphabets[new_position]
        else:
            encrypted_message += char
    # print(f"Here is the encrypted message: {encrypt_message}")
    return encrypted_message


def decryption(cipher_text):
    decrypted_message = ""
    for char in cipher_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position-shift_number)%len(alphabets)
            decrypted_message += alphabets[new_position]
        else:
            decrypted_message += char
    # print(f"Here is the encrypted message: {decrypt_message}")
    return decrypted_message


def find_max_number(numbers):
    max_number = 0
    for numb in numbers:
        if max_number < numb:
            max_number = numb
    return max_number