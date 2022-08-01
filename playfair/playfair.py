# This is the Playfiar Cipher

def playfair(strng, key, encode=True):
    AZ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    diagram = []
    row = []

    # -----Diagram-----

    # Convert key to upper + no space
    key = key.upper()
    key = key.replace(' ','')

    # Create beginning of diagram using key
    for letter in key:
        if letter == 'J': letter = 'I'

        if len(row) < 5 and letter in AZ:
            row.append(letter)
            AZ = AZ.replace(letter, '')
        elif letter in AZ:
            diagram.append(row)
            row = []
            row.append(letter)
            AZ = AZ.replace(letter, '')

    # Fill in rest of diagram using remaining AZ
    for letter in AZ:
        if letter == 'J': letter = 'I'

        if len(row) < 5 and letter in AZ:
            row.append(letter)
            AZ = AZ.replace(letter, '')
        elif letter in AZ:
            diagram.append(row)
            row = []
            row.append(letter)
            AZ = AZ.replace(letter, '')
    # Append last row to diagram
    diagram.append(row)

    # -----Format Strng----- 

    # Convert strng to upper + no space
    strng = strng.upper()
    strng = strng.replace(' ', '')

    # Split strng into pairs
    # If pair is two of the same letter,
    # Add 'X' between them
    pair = []
    plain_text = []
    for letter in strng:
        if len(pair) == 1:
            if pair[0] == letter:
                pair.append('X')
                plain_text.append(pair)
                pair = [letter]
            else:
                pair.append(letter)
                plain_text.append(pair)
                pair = []
        else:
            pair.append(letter)
    # Check if there is a leftover letter in pair.
    # If so, add 'X' and append to plain_text
    if len(pair) == 1:
        pair.append('X')
        plain_text.append(pair)


    # -----Encode-----
    if encode:
        encoded = []
        for pair in plain_text:
            coord_a = []
            coord_b = []
            for row in diagram:
                if pair[0] in row:
                    coord_a.append(diagram.index(row))
                    coord_a.append(diagram[diagram.index(row)].index(pair[0]))
                if pair[1] in row:
                    coord_b.append(diagram.index(row))
                    coord_b.append(diagram[diagram.index(row)].index(pair[1]))
            return coord_a, coord_b




print(playfair('hello', 'quiet'))

