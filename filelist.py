import os
import random
import string
import shutil
import config
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend



def list_files_in_folder(folder_path):
    files = os.listdir(folder_path)
    return files


def generate_new_names(file_names):
    new_names = []
    for _ in range(len(file_names)):
        new_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=14))
        new_name = new_name + ".bin"
        new_names.append(new_name)
    return new_names


def create_name_mapping(file_names, new_names, output_file):
    name_mapping = {new_name: original_name for original_name, new_name in zip(file_names, new_names)}

    with open(output_file, 'w') as f:
        for original_name, new_name in zip(file_names, new_names):
            line = f"{original_name} : {new_name}\n"
            f.write(line)


def extract_original_names(log_file, new_names):
    original_names = {}
    with open(log_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            parts = line.strip().split(':')
            if len(parts) == 2:
                new_name = parts[1].strip()
                original_name = parts[0].strip()
                if new_name in new_names:
                    original_names[new_name] = original_name
    return original_names
