import subprocess

while True:
    user_input = input("\n Enter 1 to Encrypt file\n Enter 2 to Decrypt file\n or 0 to exit \n Input: ")

    if user_input == '1':
        subprocess.run(['python3', 'encryptMainFile.py'])
    elif user_input == '2':
        subprocess.run(['python3', 'decryptMainFile.py'])
    elif user_input == '0':
        print("Exiting program.")
        break
    else:
        print("Invalid input. Please enter 1, 2, or 0.")