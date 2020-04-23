from coder import CaesarEncode, CaesarDecode, VigenereEncode, VigenereDecode
from hacking import ModelBuilder, Hack
import argparse
import sys
import json


def get_message(arguments):
    if arguments.input_file:
        message = arguments.input_file.read()
    else:
        message = sys.stdin.read()
    return message


def write(coder, arguments, message):
    if arguments.output_file:
        arguments.output_file.write(coder.encode(message))
    else:
        sys.stdout.write(coder.encode(message))


def encode(arguments):
    message = get_message(arguments)
    if arguments.cipher == 'caesar':
        coder = CaesarEncode(int(arguments.key))
    else:
        coder = VigenereEncode(arguments.key)
    write(coder, arguments, message)


def decode(arguments):
    message = get_message(arguments)
    if arguments.cipher == 'caesar':
        coder = CaesarDecode(int(arguments.key))
    else:
        coder = VigenereDecode(arguments.key)
    write(coder, arguments, message)


def train(arguments):
    if arguments.text_file:
        training_text = arguments.text_file.read()
    else:
        training_text = sys.stdin.read()

    arguments.model_file.write(ModelBuilder().json_model(training_text))


def hack(arguments):
    if arguments.input_file:
        message = arguments.input_file.read()
    else:
        message = sys.stdin.read()

    model = json.load(arguments.model_file)

    if arguments.output_file:
        arguments.output_file.write(Hack(model).hacking(message))
    else:
        sys.stdout.write(Hack(model).hacking(message))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    parser_for_encode = subparsers.add_parser('encode')
    parser_for_encode.set_defaults(mode='encode', func=encode)
    parser_for_encode.add_argument('--cipher', type=str, choices=['caesar', 'vigenere'], required=True)
    parser_for_encode.add_argument('--key', required=True)
    parser_for_encode.add_argument('--input-file', type=argparse.FileType('r'), required=False)
    parser_for_encode.add_argument('--output-file', type=argparse.FileType('w'), required=False)

    parser_for_decode = subparsers.add_parser('decode')
    parser_for_decode.set_defaults(mode='decode', func=decode)
    parser_for_decode.add_argument('--cipher', type=str, choices=['caesar', 'vigenere'], required=True)
    parser_for_decode.add_argument('--key', required=True)
    parser_for_decode.add_argument('--input-file', type=argparse.FileType('r'), required=False)
    parser_for_decode.add_argument('--output-file', type=argparse.FileType('w'), required=False)

    parser_for_train = subparsers.add_parser('train')
    parser_for_train.set_defaults(func=train)
    parser_for_train.add_argument('--text-file', type=argparse.FileType('r'), required=False)
    parser_for_train.add_argument('--model-file', type=argparse.FileType('w'), required=True)

    parser_for_hack = subparsers.add_parser('hack')
    parser_for_hack.set_defaults(func=hack)
    parser_for_hack.add_argument('--input-file', type=argparse.FileType('r'), required=False)
    parser_for_hack.add_argument('--output-file', type=argparse.FileType('w'), required=False)
    parser_for_hack.add_argument('--model-file', type=argparse.FileType('r'), required=True)

    parsed_arguments = parser.parse_args()
    parsed_arguments.func(parsed_arguments)
