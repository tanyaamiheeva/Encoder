from coder import CaesarDecode
from collections import defaultdict
import string
import json


class ModelBuilder:
    def __init__(self):
        self.letter_number = 0
        self.quantities = defaultdict(int)

    def count_quantity(self, text: str):
        for symbol in text.lower():
            if symbol.isalpha():
                self.quantities[symbol] += 1
                self.letter_number += 1

    def build_model(self, text: str):
        self.count_quantity(text)
        frequencies = {}
        for symbol in self.quantities:
            frequencies[symbol] = self.quantities[symbol] / self.letter_number

        return frequencies

    def json_model(self, text):
        model = json.dumps(self.build_model(text))
        return model


class Hack:
    def __init__(self, model, degree=2):
        self.model = model
        self.key = 0
        self.alphabet = string.ascii_letters
        self.degree = degree

    def count(self, new_model, shift):
        result = 0
        for symbol in string.ascii_lowercase:
            code = (string.ascii_lowercase.find(symbol) + shift) % len(string.ascii_lowercase)
            new_symbol = string.ascii_lowercase[code]
            result += (self.model[symbol] - new_model[new_symbol]) ** self.degree
        return result

    def encode(self, message: str):
        results = [0 for i in range(len(string.ascii_lowercase))]
        closest_result = 0
        new_model = ModelBuilder().build_model(message.lower())
        results[closest_result] = self.count(new_model, 0)

        for i in range(len(string.ascii_lowercase)):
            results[i] = self.count(new_model, i)
            if results[i] < results[closest_result]:
                closest_result = i

        return CaesarDecode(closest_result).encode(message)

