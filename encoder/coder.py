import string
import abc


class Coder(abc.ABC):
    __metaclass__ = abc.ABCMeta

    def __init__(self, key):
        self.key = key
        self.alphabet = string.ascii_letters

    @abc.abstractmethod
    def get_symbol(self, symbol: str, position: int):
        pass

    def encode(self, message: str):
        encoded = []
        position = 0

        for symbol in message:
            if symbol.isalpha():
                encoded.append(self.get_symbol(symbol, position))
                position += 1
            else:
                encoded.append(symbol)

        return ''.join(encoded)


class CaesarEncode(Coder):
    def __init__(self, key):
        super().__init__(key)
        self.key = int(key % (len(self.alphabet) // 2))

    def get_symbol(self, symbol: str, position: int):
        start = self.alphabet.find('A') if symbol.isupper() else self.alphabet.find('a')
        new_symbol_code = start + (self.alphabet.find(symbol) - start + self.key) % (len(self.alphabet) // 2)
        new_symbol = self.alphabet[int(new_symbol_code)]
        return new_symbol


class CaesarDecode(CaesarEncode):
    def __init__(self, key):
        super().__init__(key)
        self.key = int(((len(self.alphabet) // 2) - key) % (len(self.alphabet) // 2))


class VigenereEncode(Coder):
    def __init__(self, key: str):
        key = key.lower()
        super().__init__(key)

    def get_symbol(self, symbol: str, pos: int):
        start = self.alphabet.find('A') if symbol.isupper() else self.alphabet.find('a')
        new_symbol_code = start + (self.alphabet.find(symbol) + self.alphabet.find(self.key[pos % len(self.key)])
                                   - start - self.alphabet.find('a')) % (len(self.alphabet) // 2)
        new_symbol = self.alphabet[int(new_symbol_code)]
        return new_symbol


class VigenereDecode(Coder):
    def __init__(self, key: str):
        key = key.lower()
        super().__init__(key)

    def get_symbol(self, symbol: str, pos: int):
        start = self.alphabet.find('A') if symbol.isupper() else self.alphabet.find('a')
        real_symbol_code = start + (self.alphabet.find(symbol) - start -
                                    self.alphabet.find(self.key[pos % len(self.key)]) + self.alphabet.find('a') +
                                    (len(self.alphabet) // 2)) % (len(self.alphabet) // 2)
        real_symbol = self.alphabet[int(real_symbol_code)]
        return real_symbol
