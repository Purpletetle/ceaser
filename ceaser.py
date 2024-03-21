
plainText = input("Enter the plain text message: ")
key = int(input("Enter the key: "))

def caesarsCipher(plainText, key):
    cipherText = ""
    for char in plainText
        if char.isalpha():
            if char.islower():
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
