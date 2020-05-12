import string
import abc
FIRST_UPPERCASE_LETTER = string.ascii_uppercase[0]
FIRST_LOWERCASE_LETTER = string.ascii_lowercase[0]


class Coder(abc.ABC):
    __metaclass__ = abc.ABCMeta

    def __init__(self, key):
        self.key = key
        self.alphabet = string.ascii_letters

    @abc.abstractmethod
    def get_symbol(self, symbol: str, position: int):
        pass

    def get_start(self, symbol):
        start = self.alphabet.find(FIRST_UPPERCASE_LETTER) if symbol.isupper() else \
            self.alphabet.find(FIRST_LOWERCASE_LETTER)
        return start

    def encode(self, message: str):
        encoded = [''] * len(message)
        position = 0

        for i, symbol in enumerate(message):
            if symbol.isalpha():
                encoded[i] = self.get_symbol(symbol, position)
                position += 1
            else:
                encoded[i] = symbol

        return ''.join(encoded)


class CaesarEncode(Coder):
    def __init__(self, key):
        super().__init__(key)
        self.key = int(key % (len(self.alphabet) // 2))

    def get_symbol(self, symbol: str, position: int):
        start = self.get_start(symbol)
        new_symbol_code = start + (self.alphabet.find(symbol) - start + self.key) % (len(self.alphabet) // 2)
        new_symbol = self.alphabet[int(new_symbol_code)]
        return new_symbol


class CaesarDecode(CaesarEncode):
    def __init__(self, key):
        super().__init__(key)
        self.key *= -1


class VigenereEncode(Coder):
    def __init__(self, key: str):
        key = key.lower()
        super().__init__(key)

    def get_symbol(self, symbol: str, pos: int):
        start = self.get_start(symbol)
        new_symbol_code = start + (self.alphabet.find(symbol) + self.alphabet.find(self.key[pos % len(self.key)])
                                   - start - self.alphabet.find(FIRST_LOWERCASE_LETTER)) % (len(self.alphabet) // 2)
        new_symbol = self.alphabet[int(new_symbol_code)]
        return new_symbol


class VigenereDecode(Coder):
    def __init__(self, key: str):
        key = key.lower()
        super().__init__(key)

    def get_symbol(self, symbol: str, pos: int):
        start = self.get_start(symbol)
        real_symbol_code = start + (self.alphabet.find(symbol) - start -
                                    self.alphabet.find(self.key[pos % len(self.key)]) +
                                    self.alphabet.find(FIRST_LOWERCASE_LETTER) +
                                    (len(self.alphabet) // 2)) % (len(self.alphabet) // 2)
        real_symbol = self.alphabet[int(real_symbol_code)]
        return real_symbol

