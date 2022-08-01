# This is a decryption tool for the ROT-13 Ceasar Cipher

def decrypt_rot(strng):
    az = 'abcdefghijklmnopqrstuvwxyz'
    decrypted = ''
    for i in strng:
        if i.isalpha():
            if i.islower():
                if az.index(i) < 13:
                    decrypted += az[az.index(i) + 13]
                elif az.index(i) >= 13:
                    decrypted += (az[(az.index(i) + 13) % 13])
            else:
                if az.upper().index(i) < 13:
                    decrypted += az.upper()[az.upper().index(i) + 13]
                elif az.upper().index(i) >= 13:
                    decrypted += az.upper()[(az.upper().index(i) + 13) % 13]
        else:
            decrypted += i
    return decrypted
code = input('Enter the text: ')
print(decrypt_rot(code))
