
plainText = input("Enter the plain text message: ")
key = int(input("Enter the key: "))

def caesarsCipher(plainText, key):
    cipherText = ""
    for char in plainText:
        # Let's check if the character is a letter
        if char.isalpha():
            # Let's check if the character is upper or lower case
            if char.islower():
                # chr returns the character that corresponds to the ASCII code
                # ord returns the ASCII code that corresponds to the character
                # We use the ASCII code to shift the character by the key
                # We use the modulo operator to wrap around the alphabet
                cipherText += chr((ord(char) + key - 97) % 26 + 97)
            else:
                cipherText += chr((ord(char) + key - 65) % 26 + 65)
        else:
            cipherText += char
    return cipherText

print(caesarsCipher(plainText, key))

print("To test the decipher function, enter the ciphered message and the negative key")
cipher = input("Enter the ciphered message: ")
key = int(input("Enter the key: "))

print(caesarsCipher(cipher, key))
