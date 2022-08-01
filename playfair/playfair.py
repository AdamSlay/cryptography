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
        # Rule 1: If they are on same row, add/sub 1 from row
        if coord_a[0] == coord_b[0]:
            if encode:
                encoded.append(diagram[coord_a[0]][(coord_a[1] + 1) % 5])
                encoded.append(diagram[coord_b[0]][(coord_b[1] + 1) % 5])
            else:
                # is the col index 0?
                if coord_a[1] == 0:
                    encoded.append(diagram[coord_a[0]][4])
                else:
                    encoded.append(diagram[coord_a[0]][coord_a[1] - 1])
                if coord_b[1] == 0:
                    encoded.append(diagram[coord_b[0]][4])
                else:
                    encoded.append(diagram[coord_b[0]][coord_b[1] - 1])
        # Rule 2: If they are on the same col, add/sub 1 from col
        elif coord_a[1] == coord_b[1]:
            if encode:
                encoded.append(diagram[(coord_a[0] + 1) % 5][coord_a[1]])
                encoded.append(diagram[(coord_b[0] + 1) % 5][coord_b[1]])
            else:
                # is the row index 0?
                if coord_a[0] == 0:
                    encoded.append(diagram[coord_a[4]][coord_a[1]])
                else:
                    encoded.append(diagram[coord_a[0] - 1][coord_a[1]])
                if coord_b[0] == 0:
                    encoded.append(diagram[coord_b[4]][coord_b[1]])
                else:
                    encoded.append(diagram[coord_b[0] - 1][coord_b[1]])
        # Rule 3: Make square and grab opposite corner on same row
        else:
            encoded.append(diagram[coord_a[0]][coord_b[1]])
            encoded.append(diagram[coord_b[0]][coord_a[1]])

    return ''.join(encoded)

# Test
#print(playfair('QKSUSULUCBSO', 'quiet', False))

