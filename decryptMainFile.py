from filelist import *
from decrypt import *
import subprocess


key_file = config.key_file
log_file = config.log_file

encrypted_folder_path = config.encrypted_folder_path
decrypted_folder_path = config.decrypted_folder_path


deOrNot = input("\n\n Do you want to decrypt the file? You can only decrypt it once.\n If someone decrypts it incorrectly, you won't be able to decrypt the file again,\n and it will remain permanently undecrypted.\n\n Enter 1 or 0: ")


if deOrNot == '1':
    folder_exists = all(os.path.exists(folder) for folder in [encrypted_folder_path, decrypted_folder_path])

    if folder_exists:
        with open(key_file, 'rb') as f:
            key = f.read() 

        with open(log_file, 'rb') as f:
            ciphertext_with_iv = f.read()

        decrypt_file_function(key, ciphertext_with_iv, log_file)

        file_names = list_files_in_folder(encrypted_folder_path)
        original_names = extract_original_names(log_file, file_names)

        for file_names, original_name in original_names.items():
            original_name = decrypted_folder_path + original_name
            encrypt_file_name = encrypted_folder_path + file_names
            with open(encrypt_file_name, 'rb') as f:
                ciphertext_with_iv = f.read()
            
            decrypt_file_function(key, ciphertext_with_iv, original_name)  

                
        print("Encrypted data Decrypted to:")
        for key, value in original_names.items():
            print(f"{key}: {value}")

    else :
        print("Folder not exist!!!")


elif deOrNot == '0':
    print("")
