# Task 1 - Vigenere Cipher                     #
# Authors:                                     #
#           Rodrigo Martin Shiller - 313722597 #
#           Mark Davydov           - 321894925 #
################################################
def Cipher(plainText, key, mode):
    cipherText = ""
    for i in range(0, len(plainText)):
        if mode == '1': # Cipher
            ci = (ord(plainText[i]) + ord(key[i % len(key)])) % 26   # Ci cipher calculation.
        else:  # Decipher if key is known
            ci = (ord(plainText[i]) - ord(key[i % len(key)])) % 26
        cipherText += chr(ci + 65)  # Adding 65 in order to get the uppercased ciphered letter.
    return cipherText

while True:
    mode = input("Please select your mode (cipher '1' | decipher '2'): ")
    if mode == '1' or mode == '2':
        break
    else:
        print("Only '1' or '2'.")

while True:
    isKeyKnown = input("Do you know the key for the cipher? ")

while True:
    plainText = input("Please insert text to cipher: ")
    if plainText.replace(" ", "").isalpha():
        break
    else: print("Only alphabetical characters allowed.")

while True:
    key = input("Please insert a key for the cipher: ")
    if key.replace(" ", "").isalpha():
        break
    else: print("Only alphabetical characters allowed.")

# Arrange the text in correct format for cipher:
plainText = ''.join(plainText.split()).upper()
key = ''.join(key.split()).upper()

print(plainText+'\n'+key) # TEST PRINT

print("Cipher Text  =", Cipher(plainText, key, mode))
print("Suposed Text = ISWXVIRMSVTAYUFZCHNYFJQRLBQC")