import random

file = open('./plaintext.txt', 'r')

plaintext = file.read()
ciphertext = ""
shift = random.randint(1, 26)

for char in plaintext:
    newChar = chr( ord(char) + shift )
    ciphertext = ciphertext + newChar

print(ciphertext)

file.close()