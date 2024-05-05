# Cypher

Cypher is a simple Python script that allows you to encrypt or decrypt text or a file using a key and a salt.

## Usage

You can use Cypher from the command line with the following arguments:

`-t` or `--text`: The text to encrypt or decrypt.
`-k` or `--key`: The encryption key. This is required.
`-m `or `--mode`: The mode of operation. Use e for encryption and d for decryption. This is required.
`-f` or `--file`: The file to encrypt or decrypt.
You will also be prompted to enter a salt when you run the script.

Here are some examples of how to use Cypher:

```
# Encrypt text
python cypher.py -t "Hello, World!" -k mykey -m e

# Decrypt text
python cypher.py -t "Encrypted text" -k mykey -m d

# Encrypt a file
python cypher.py -f myfile.txt -k mykey -m e

# Decrypt a file
python cypher.py -f myfile.txt -k mykey -m d
```

# Important

Please remember that the security of your encrypted data is entirely dependent on the strength and secrecy of your key and salt. Do not use this script for serious cryptographic needs. It is a simple demonstration of encryption and decryption in Python.
