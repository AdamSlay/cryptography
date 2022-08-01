# This is the Playfiar Cipher

def playfair(strng, key, encode=True):
    AZ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    diagram = []
    d = []

    # Convert key to upper + no space
    key = key.upper()
    key = key.replace(' ','')

    # Create beginning of diagram using key
    for letter in key:
        if letter == 'J': letter = 'I'

        if len(d) < 5 and letter in AZ:
            d.append(letter)
            AZ = AZ.replace(letter, '')
        elif letter in AZ:
            diagram.append(d)
            d = []
            d.append(letter)
            AZ = AZ.replace(letter, '')

    # Fill in rest of diagram using remaining AZ
    for letter in AZ:
        if letter == 'J': letter = 'I'

        if len(d) < 5 and letter in AZ:
            d.append(letter)
            AZ = AZ.replace(letter, '')
        elif letter in AZ:
            diagram.append(d)
            d = []
            d.append(letter)
            AZ = AZ.replace(letter, '')
    # Append last row to diagram
    diagram.append(d)

    return diagram

print(playfair('hello', 'quiet'))

