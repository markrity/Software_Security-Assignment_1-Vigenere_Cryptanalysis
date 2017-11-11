# Task 1 - Vigenere Cipher                     #
# Authors:                                     #
#           Rodrigo Martin Shiller - 313722597 #
#           Mark Davydov           - 321894925 #
################################################
import re
import operator
import math
import collections


def cipher(plain_text):
    cipher_text = ""
    for i in range(0, len(plain_text)):
        ci = oprtr[mode](ord(plain_text[i]), ord(key[i % len(key)])) % 26
        cipher_text += chr(ci + 65)  # Adding 65 in order to get the uppercased ciphered letter.
    return cipher_text


def frequency(cipher_text):
    temp_cipher = cipher_text
    count = [0]*26  # This array represents the histogram of frequencies of each character in the text

    while True:     # Counting and saving to the array the amount of appearances of a certain character
        if temp_cipher == '':   # If the work is done
            break
        count[ord(temp_cipher[0])-65] = temp_cipher.count(temp_cipher[0]) # Storing in an array how many times a character appears.
        # count.append(temp_cipher.count(temp_cipher[0]))
        temp_cipher = re.sub('['+temp_cipher[0]+']', '', temp_cipher)  # Remove all the appearances a character

    return count


def index_of_coincidence():
    ic = [0]*15
    col = []
    a = []
    j = 0
    for k in range(1, 16):
        x = math.ceil(k / len(text))
        # a = [['-' for i in range(16)] for j in range(x)]
        txt = ''
        for i in range(len(text)):
            if i == len(text) or i+k >= len(text):
                break
            else:
                txt += text[i]



       # for i in range(0, len(text)):
        b = [text[j] for j in range(0, len(text), k)]
       # c = [sum(frequency(b[i])) for i in range(len(b))]
        print(b)
        a.append(b)
    d = []
    print('A:\n', a)




   # N = len(text)
   # ic = 0
   # for n in frequency(text):
   #     ic += n*(n-1)
   # return ic / (N*(N-1)/26)

    #f = 0
    #or i in frequency(text):  # Calculating the occurrences of all the characters
    #    f += i*(i-1)
    #return f / (len(text) * (len(text) - 1))  # Returning the index of coincidence


def kasisky():
    print('Kasisky')


def get_text():
    while True:
        plainText = ''.join(input("Please insert text to cipher: ").split()).upper()
        if plainText.isalpha():
            return plainText
        else:
            print("Only alphabetical characters allowed.")


def get_key():
    while True:
        key = ''.join(input("Please insert a key for the cipher: ").split()).upper()
        if key.isalpha():
            return key
        else:
            print("Only alphabetical characters allowed.")



oprtr = {"1": operator.add,
         "2": operator.sub}

while True:
    mode = input("Please select your mode (cipher '1' | decipher '2'): ")
    if mode == '1' or mode == '2':
        break
    else:
        print("Only '1' or '2' characters allowed.")

text = get_text()
key = ''
print(collections.Counter(text))
if mode == '2':
    isKeyKnown = '-1'
    while True:
        isKeyKnown = input("Do you know the key for the cipher (y/n)? ").upper()
        if isKeyKnown == 'Y' or isKeyKnown == 'N':
            break
        else:
            print("Only 'y' or 'n' characters allowed.")
    if isKeyKnown != '-1' and isKeyKnown == 'N':
        print(index_of_coincidence())
       # print(frequency(text))
    elif isKeyKnown == 'Y':
        key = get_key()
        print(cipher(text))

else:
    print(text+'\n'+key)  # TEST PRINT

    print("Cipher Text  =", cipher(text))
    print("Suposed Text = ISWXVIRMSVTAYUFZCHNYFJQRLBQC")