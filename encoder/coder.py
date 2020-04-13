class CaesarEncode:
    def __init__(self, key):
        self.key = int(key) % 26

    def get_new_symbol(self, symbol: str):
        if not symbol.isalpha():
            return symbol
        else:
            if symbol.isupper():
                start = ord('A')
            else:
                start = ord('a')

            new_symbol_code = start + (ord(symbol) - start + self.key) % 26
            new_symbol = chr(new_symbol_code)
            return new_symbol

    def encoder(self, message: str):
        encoded = []

        for symbol in message:
            encoded.append(CaesarEncode.get_new_symbol(self, symbol))

        return ''.join(encoded)


class CaesarDecode:
    def __init__(self, key):
        self.key = int(key) % 26

    def get_real_symbol(self, symbol: str):
        if not symbol.isalpha():
            return symbol
        else:
            if symbol.isupper():
                start = ord('A')
            else:
                start = ord('a')

            real_symbol_number = start + (ord(symbol) - start + 26 - self.key) % 26
            real_symbol = chr(real_symbol_number)
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
            start = ord('A')
        else:
            start = ord('a')

        new_symbol_code = start + (ord(symbol) + ord(self.key[pos % len(self.key)]) - start - ord('a')) % 26
        new_symbol = chr(new_symbol_code)
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
            start = ord('A')
        else:
            start = ord('a')

        real_symbol_code = start + (ord(symbol) - start - ord(self.key[pos % len(self.key)]) + ord('a') + 26) % 26
        real_symbol = chr(real_symbol_code)
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
