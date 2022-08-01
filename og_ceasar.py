# The OG Caesar Cipher


def og_caes(strng):
    az = 'abcdefghijklmnopqrstuvwxyz'
    new = ''
    for i in strng:
        new += az[(az.index(i) + 3) % 26]
    return new

print(og_caes('attackatdawn'))

