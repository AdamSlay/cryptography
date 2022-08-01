# Vigenere Cipher Encoder/Decoder

class VigenereCipher(object):

    def __init__(self, key, alph):
        self.key = key
        self.alph = alph


    def encode(self, text):
        pass_repeat = []
        encoded = ''

        for position,value in enumerate(text):
            pass_repeat.append(self.key[position % len(self.key)])

            if value in self.alph:
                alph_position = self.alph.index(value)
                pass_position = self.alph.index(pass_repeat[position])
                encoded += self.alph[(alph_position + pass_position) % len(self.alph)]
            else:
                encoded += value

        return encoded


    def decode(self, text):
        pass_repeat = []
        decoded = ''

        for position,value in enumerate(text):
            pass_repeat.append(self.key[position % len(self.key)])

            if value in self.alph:
                alph_position = self.alph.index(value)
                pass_position = self.alph.index(pass_repeat[position])
                if alph_position >= pass_position:
                    decoded += self.alph[abs(alph_position - pass_position) % len(self.alph)]
                else:
                    decoded += self.alph[len(self.alph) - abs(alph_position - pass_position)]
            else:
                decoded += value
        return decoded


# Tests
abc = 'abcdefghijklmnopqrstuvwxyz'
key = 'password'
c = VigenereCipher(key, abc)
print(c.decode('CODEWARS'))
