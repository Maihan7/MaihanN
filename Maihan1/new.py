import math

#encryption

def encrypt():
 plainText = input("Please insert a text to encrypt: ")
 key = int(input("How much is the key lenght?: "))
 plainText= ''.join(plainText.split(' '))
 columns = [];
 for i in range(key):
    columns.append(plainText[i::key])
 print(columns)
encrypt()

#Decryption
def decrypt():
 encryptedText = input("Please insert a text to decrypt: ").replace(" ","")
 key = int(input("How much is the key lenght?: "))
 encryptedText = ''.join(encryptedText.split(' '))
 rows=math.ceil(len(encryptedText)/key)
 plainTXT = [];
 for i in range(rows):
    plainTXT.append(encryptedText[i::rows])
 print(plainTXT)
decrypt()