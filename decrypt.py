from filelist import *


def decode_binary_string(binary_string, encodings=['utf-8', 'latin-1', 'ascii']):
    for encoding in encodings:
        try:
            text_string = binary_string.decode(encoding)
            return text_string
        except UnicodeDecodeError:
            pass
    return None


def decrypt_file_function(key, ciphertext_with_iv, original_name):
    iv = ciphertext_with_iv[:16]  # Extract IV from the ciphertext
    ciphertext = ciphertext_with_iv[16:]  # Extract ciphertext without IV

       # Initialize ChaCha20-Poly1305 cipher for decryption
    cipher = Cipher(algorithms.ChaCha20(key, iv), mode=None, backend=default_backend())
    decryptor = cipher.decryptor()  # Create a decryptor object
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()  # Decrypt the ciphertext

    with open(original_name, 'wb') as f:  # Write decrypted data to the output file
        f.write(decrypted_data)

    ### If you want to show data on terminal
    # text_string = decode_binary_string(decrypted_data)
    # if text_string is not None:
    #     print("Decoded text:", text_string)
    # else:
    #     print("Unable to decode binary string with any of the specified encodings.")
