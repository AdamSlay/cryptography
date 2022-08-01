# This is the Playfair Cipher. 

## History
The Playfair Cipher was originlly described by Charles Wheatstone in 1854, but 
gets its name from Lord Playfair who promoted its use.It was the first cipher 
that we know of which encrypted pairs of letters at a time rather than each 
letter individually. This method of encryption was far more difficult to break
than something like the Vigenere Cipher. 

## Usage:
The idea of the Playfair Cipher is to create a **5x5** diagram using a keyword.
Each letter of the alphabet is only used once when filling out the diagram.
The keyword is used as the beginning of the diagram, filling as many spaces
as necessary, then the remaining letters of the alphabet make up the rest of the
diagram. Here is an example diagram using the keyword 'PLAYFAIR'.

1 | 2 | 3 | 4 | 5 
--- | --- | --- | --- | ---
P | L | A | Y | F
I | R | B | C | D
E | G | H | J | K
M | N | O | Q | S
T | U | V | W | X


Uses a keyword to generate the  5x5 table
Replace *pairs* of letters from the original string rather than each letter
Use the following **4** rules for encryption:

1. if both letters in the pair are the same, add an 'X' between them to separate 
them into distinct pairs.
2. if they appear in the same row of the diagram, shift each letter one space
to the *right*, wrapping around the table if needed.
3. if they appear in the same column, shift each letter *down* one space. 
4. If they form the corners of a rectangle, replace them with the characters
forming the opposing corners of the rectangle.
