import string
alphabet = string.ascii_lowercase + string.ascii_uppercase


class CaesarEncode:
    def __init__(self, key):
        self.key = int(key % (len(alphabet) / 2))

    def get_new_symbol(self, symbol: str):
        if not symbol.isalpha():
            return symbol
        else:
            if symbol.isupper():
                start = alphabet.find('A')
            else:
                start = alphabet.find('a')

            new_symbol_code = start + (alphabet.find(symbol) - start + self.key) % (len(alphabet) / 2)
            new_symbol = alphabet[int(new_symbol_code)]
            return new_symbol

    def encoder(self, message: str):
        encoded = []

        for symbol in message:
            encoded.append(CaesarEncode.get_new_symbol(self, symbol))

        return ''.join(encoded)


class CaesarDecode:
    def __init__(self, key):
        self.key = int(key % (len(alphabet) / 2))

    def get_real_symbol(self, symbol: str):
        if not symbol.isalpha():
            return symbol
        else:
            if symbol.isupper():
                start = alphabet.find('A')
            else:
                start = alphabet.find('a')

            real_symbol_number = int(start + (alphabet.find(symbol) - start +
                                              (len(alphabet) / 2) - self.key) % (len(alphabet) / 2))
            real_symbol = alphabet[real_symbol_number]
            return real_symbol

    def decoder(self, message: str):
        decoded = []

        for symbol in message:
            decoded.append(CaesarDecode.get_real_symbol(self, symbol))

        return ''.join(decoded)


class VigenereEncode:
    def __init__(self, key: str):
        self.key = key.lower()

    def get_new_symbol(self, symbol: str, pos: int):
        if symbol.isupper():
            start = alphabet.find('A')
        else:
            start = alphabet.find('a')

        new_symbol_code = int(start + (alphabet.find(symbol) + alphabet.find(self.key[pos % len(self.key)])
                                       - start - alphabet.find('a')) % (len(alphabet) / 2))
        new_symbol = alphabet[new_symbol_code]
        return new_symbol

    def encoder(self, message: str):
        encoded = []
        position = 0

        for symbol in message:
            if symbol.isalpha():
                encoded.append(VigenereEncode.get_new_symbol(self, symbol, position))
                position += 1
            else:
                encoded.append(symbol)

        return ''.join(encoded)


class VigenereDecode:
    def __init__(self, key: str):
        self.key = key.lower()

    def get_real_symbol(self, symbol: str, pos: int):
        if symbol.isupper():
            start = alphabet.find('A')
        else:
            start = alphabet.find('a')

        real_symbol_code = int(start + (alphabet.find(symbol) - start - alphabet.find(self.key[pos % len(self.key)])
                                        + alphabet.find('a') + (len(alphabet) / 2)) % (len(alphabet) / 2))
        real_symbol = alphabet[real_symbol_code]
        return real_symbol

    def decoder(self, message: str):
        decoded = []
        position = 0

        for symbol in message:
            if symbol.isalpha():
                decoded.append(VigenereDecode.get_real_symbol(self, symbol, position))
                position += 1
            else:
                decoded.append(symbol)
        return ''.join(decoded)
