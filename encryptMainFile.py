from filelist import *
from encrypt import *
from key import generate_key


key_file = config.key_file
log_file = config.log_file
password = config.password
original_folder_path = config.original_folder_path
encrypted_folder_path = config.encrypted_folder_path


folder_exists = all(os.path.exists(folder) for folder in [original_folder_path, encrypted_folder_path])

if folder_exists:
    salt = os.urandom(16)
    key = generate_key(password, salt)

    file_names = list_files_in_folder(original_folder_path)

    new_names = generate_new_names(file_names)

    create_name_mapping(file_names, new_names, log_file)

    encrypt_file(key, file_names, new_names, original_folder_path, encrypted_folder_path)

    with open(key_file, 'wb') as f:
        f.write(key)
    encrypt_file_function(key, log_file, log_file)

    # shutil.rmtree(original_folder_path)
else:
    print("Folder not exist!!!")