import random

file = open('./plaintext.txt', 'r', encoding = "utf-8")

plaintext = file.read().lower().replace(" ", "")

def ceaser(plain):
    shift = random.randint(1, 26)
    ciphertext = ""
    index = 0
    for char in plaintext:
        newchar = ""
        if((ord(char) + shift) > 122):
            newChar = chr( ord(char) + shift - 26)
        else:
            newChar = chr( ord(char) + shift ) 
        ciphertext = ciphertext + newChar
        
        if(index == 4):
            index = 0
            ciphertext = ciphertext + " "
        else:
            index = index + 1
    return ciphertext

cipher = ceaser(plaintext)


output = open('./ciphertext.txt', 'w')
output.write(cipher)

file.close()