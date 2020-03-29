#!/usr/bin/python3
"""
Decrypt file and print clear text on stdout. Use private_key.pem to decrypt the file, path to file
is passed as parameter script.
"""

import sys
import pathlib

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


PATH_TO_KEY = pathlib.Path(__file__).parent / 'private_key.pem'

with open(PATH_TO_KEY, 'rb') as private_key_file:
    private_key = serialization.load_pem_private_key(
        private_key_file.read(),
        backend=default_backend(),
        password=None)

with open(sys.argv[1], 'rb') as f:
    cleartext = private_key.decrypt(
        f.read(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

print(cleartext.decode())
