exit_program = False

alphabet = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
    "k": 10,
    "l": 11,
    "m": 12,
    "n": 13,
    "o": 14,
    "p": 15,
    "r": 16,
    "s": 17,
    "t": 18,
    "q": 19,
    "u": 20,
    "v": 21,
    "w": 22,
    "x": 23,
    "y": 24,
    "z": 25,
    "_": 26,
}

# encrypts given text with given key using Vigenere's cipher
def encrypt(text, key):
    encrypted_text = ""
    # lowercase our text and remove whitespaces
    text.lower()
    text.replace(" ", "")
    key.lower()
    key.replace(" ", "")
    # encrypting whole text using Vigenere's cipher
    for el in range(len(text)):
        text_number = alphabet[text[el]]  # number assigned to specified letter
        key_number = alphabet[
            key[el % len(key)]
        ]  # we're looping using text length, so it's safe to use modulo if key's length is shorter
        encrypted_number = (
            text_number + key_number
        ) % 27  # finding number of new letter that will replace the original letter
        for alphabetkey, alphabetvalue in alphabet:
            if alphabetvalue == encrypted_number:
                encrypted_text.join(alphabetkey)

    return encrypted_text


def decrypt(text, key):
    decrypted_text = ""
    return decrypted_text


while not exit_program:
    print(
        """
    Welcome to Vingenere cipher program
    MENU:
        1. Encrypt message
        2. Decrypt message
        3. Exit
    """
    )
    answer = input("Choose option: ")
    if answer == "1":
        text = input("Enter the message you want to encrypt: ")
        key = input("Now enter the key you want to use: ")
        print("Encrypted message: " + encrypt(text, key) + "\n")
    elif answer == "2":
        text = input("Enter the message you want to decrypt: ")
        key = input("Now enter the key that was used to encrypt the message: ")
        print("Decrypted message: " + decrypt(text, key) + "\n")
    elif answer == "3":
        exit_program = True
    else:
        answer = input("Error, please choose your option again: ")
