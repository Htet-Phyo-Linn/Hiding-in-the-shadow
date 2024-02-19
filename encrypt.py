from filelist import *


def encrypt_file_function(key, input_file, output_file):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.ChaCha20(key, iv), mode=None)
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()

    with open(input_file, 'rb') as f:
            plaintext = f.read()

    padded_data = padder.update(plaintext) + padder.finalize()

        # Encrypt the padded data
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

        # Write the IV concatenated with the ciphertext to the output file
    with open(output_file, 'wb') as f:
        f.write(iv + ciphertext)


def encrypt_file(key, file_names, new_names, input_folder_path, output_folder_path):
    assert len(file_names) == len(new_names), "Length of file_names and new_names must be the same"
    
    for input_file, output_file in zip(file_names, new_names):
        input_file = input_folder_path + input_file

        output_file = output_folder_path + output_file

        encrypt_file_function(key, input_file, output_file)

        print("Encryption complete for:", input_file, "->", output_file, "\n")
