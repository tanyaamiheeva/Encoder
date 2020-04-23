from coder import CaesarEncode, CaesarDecode
from collections import defaultdict
import string
import json


class ModelBuilder:
    def __init__(self):
        self.letter_number = 0
        self.quantities = defaultdict(int)

    def count_quantity(self, text: str):
        for symbol in text:
            if symbol.isalpha():
                self.quantities[symbol] += 1
                self.letter_number += 1

    def build_model(self, text: str):
        self.count_quantity(text)
        frequencies = {}
        for symbol in self.quantities.keys():
            frequencies[symbol] = self.quantities.get(symbol, 0) / self.letter_number

        return frequencies

    def json_model(self, text):
        model = json.dumps(self.build_model(text))
        return model


class Hack:
    def __init__(self, model):
        self.model = model
        self.key = 0
        self.alphabet = string.ascii_letters

    def hacking(self, message: str):
        closest_key = 0
        closest_sum = 100
        for i in range(len(self.alphabet) // 2):
            encoded = CaesarEncode(i).encode(message)
            new_model = ModelBuilder().build_model(encoded)
            similarity_measure = 0
            for symbol in string.ascii_lowercase:
                similarity_measure += (self.model.get(symbol, 0) - new_model.get(symbol, 0))**6
            if similarity_measure < closest_sum:
                closest_sum = similarity_measure
                closest_key = i

        return CaesarEncode(closest_key).encode(message)