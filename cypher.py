import os
import base64
import sys
from getpass import getpass
import argparse


def encrypt(text, key, salt):
    if not key:
        raise ValueError("Key cannot be empty")
    key += salt
    result = ""
    for i in range(len(text)):
        char = text[i]
        key_c = key[i % len(key)]
        result += chr((ord(char) + ord(key_c)) % 128)
    return result


def decrypt(text, key, salt):
    if not key:
        raise ValueError("Key cannot be empty")
    key += salt
    result = ""
    for i in range(len(text)):
        char = text[i]
        key_c = key[i % len(key)]
        result += chr((ord(char) - ord(key_c)) % 128)
    return result


def handle_file(file_path, key, mode, salt):
    if not os.path.isfile(file_path):
        print(f"The file {file_path} does not exist.")
        sys.exit(1)
    with open(file_path, "r") as file:
        text = file.read()
    if mode == "e":
        result = encrypt(text, key, salt)
    else:
        result = decrypt(text, key, salt)
    with open(file_path, "w") as file:
        file.write(result)


def main():
    parser = argparse.ArgumentParser(description="Encrypt or decrypt text or a file.")
    parser.add_argument("-t", "--text", help="The text to encrypt or decrypt.")
    parser.add_argument("-k", "--key", required=True, help="The encryption key.")
    parser.add_argument(
        "-m",
        "--mode",
        choices=["e", "d"],
        required=True,
        help='Mode: "e" for encryption, "d" for decryption.',
    )
    parser.add_argument("-f", "--file", help="The file to encrypt or decrypt.")
    args = parser.parse_args()

    salt = getpass("Enter a salt: ")

    if args.text:
        if args.mode == "e":
            print("Result: " + encrypt(args.text, args.key, salt))
        else:
            print("Result: " + decrypt(args.text, args.key, salt))
    elif args.file:
        handle_file(args.file, args.key, args.mode, salt)
    else:
        print("Either text or file must be provided.")
        sys.exit(1)


if __name__ == "__main__":
    main()
