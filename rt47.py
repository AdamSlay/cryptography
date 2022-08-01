# This is a ROT-47 cipher encoder/decoder

def rot47(str):
    key = '!"#$%&' + "'" + '()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
    words = str.split(' ')
    final = []

    for word in words:
        crypted = []
        for letter in word:
            crypted.append(key[(key.index(letter) + 47) % 94])
        final.append(''.join(crypted))

    return ' '.join(final)

s = 'The Quick Brown Fox Jumps Over The Lazy Dog.'
print(rot47(s))