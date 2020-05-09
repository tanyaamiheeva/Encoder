from coder import CaesarEncode, CaesarDecode
from collections import defaultdict
from copy import deepcopy
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
        for symbol in self.quantities.keys():
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

    def hacking(self, message: str):
        results = [0 for i in range(len(self.alphabet))]
        closest_result = 0
        new_model = ModelBuilder().build_model(message.lower())
        for symbol in string.ascii_lowercase:
            results[closest_result] += (self.model.get(symbol, 0) - new_model.get(symbol, 0)) ** self.degree

        for i in range(0, len(self.alphabet) // 2):
            for symbol in string.ascii_lowercase:
                results[i] += (self.model.get(symbol, 0) - new_model.get(symbol, 0)) ** self.degree
            if results[i] < results[closest_result]:
                closest_result = i

            next_model = deepcopy(new_model)
            for letter in range(len(string.ascii_lowercase)):
                next_model[string.ascii_lowercase[letter]] = new_model[
                    string.ascii_lowercase[(letter + 1) % len(string.ascii_lowercase)]]
            new_model = next_model
        return CaesarDecode(closest_result).encode(message)

