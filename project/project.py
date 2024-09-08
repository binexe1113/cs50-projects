import csv
import os
import getpass
from cryptography.fernet import Fernet
import random
import string
import sys
import keyring
from tabulate import tabulate


# mkf=master key file #accpss = accounts pass || this just makes easier to acces the variable
mkf = "master_key.csv"
accpss = "accounts_pass.csv"
enckeyfile = "encrypted_key_file.key"
...

...


def main():
    if mkf_exister():
        verify_mk()
    else:
        create_mk()
    while True:
        user_input = menu()

        if user_input == 1:
            gerapa()
        elif user_input == 2:
            restore_password()
        elif user_input == 3:
            add_password()
        elif user_input == 4:
            decrypt_and_print_passwords()
        elif user_input == 5:
            sys.exit("exited successfully")

 # menu as a function to keep coming back to


def menu():
    print("Input a number to execute a command:")
    print("1 --- Generate a password")
    print("2 --- Restore a password")
    print("3 --- Add a password")
    print("4 --- Acces list of passwords")
    print("5 --- Exit")
    while True:
        user_input = input("").strip()
        try:
            user_choice = int(user_input)
            if user_choice in (1, 2, 3, 4, 5):
                return user_choice
            else:
                print("Please insert only 1, 2, 3, 4 or 5.")
        except ValueError:
            print("Please insert only 1, 2, 3, 4 or 5.")

 # gerapa = generate_random_password


def gerapa():
    while True:
        usrchlen = input("Insert length of password: ").strip()

        if not usrchlen.isnumeric():
            print("Insert only numbers.")
            continue
        elif int(usrchlen) < 16:
            print("Too few characters, please input a length of 16 or more.")
            continue

        # Generate the password if length is valid
        length = int(usrchlen)
        characters = string.ascii_letters + string.punctuation + string.digits
        password = ''.join(random.choice(characters) for _ in range(length))
        print(f"Generated password: {password}")

        # Ask if the user wants to save the password
        while True:
            y = input("Would you like to save this password? yes/no: ").strip().lower()
            if y.lower() in ("y", "yes", "ye"):
                name = input(
                    "insert the site name or username you would like to associate with this passowrd: ")
                savepass(name, password)
                break
            elif y.lower() not in ("n", "no", "na"):
                print("Please answer yes or no ")
            else:
                break

        # Ask if the user wants to generate another password or return to the main menu
        while True:
            z = input("Would you like to generate another password? yes/no: ").strip().lower()
            if z.lower() in ("y", "yes", "ye"):
                print("Restarting password generator...\n")
                break
            elif z.lower() in ("no", "n"):
                print("Returning to main menu \n")
                return
            else:
                print("Please insert only yes or no .")


# func to check for existence of mkf
def mkf_exister():
    return os.path.exists("master_key.csv")
# func to ask user for mk


def ask_for_mk():
    return getpass.getpass("\nEnter master key: \n")

# func to create the master key || mkf== master key file declared at the top


def create_mk():
    print("No master key found, create one to execute the program: ")
    key = getpass.getpass("Create a master key: \n")
    conf_key = getpass.getpass("Confirm the master key: \n")

    while key != conf_key:
        try:
            print("Keys do not match. Please try again.\n")
            key = getpass.getpass("Create a master key: \n")
            conf_key = getpass.getpass("Confirm the master key: \n")
        except:
            break

    if (os.path.exists(enckeyfile)) == False:
        geenkey()

    encryption_key = loenkey()

    encrypted_key = encrypt_key(key, encryption_key)

    with open(mkf, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([encrypted_key])
    print("Account created successfully!")


# func to verufy the user input is the master key
def verify_mk():
    attempts = 5
    print("\nYou only have 5 attempts, be careful.")

    with open(mkf, 'r') as file:
        reader = csv.reader(file)
        stored_encrypted_key = next(reader)[0]

    encryption_key = loenkey()
    decrypted_key = decrypt_key(stored_encrypted_key, encryption_key)

    while attempts > 0:
        entered_key = ask_for_mk()
        if entered_key == decrypted_key:
            print("Access granted.\n")
            return True
        else:
            attempts = attempts - 1
            print(f"Incorrect key. {attempts} attempt(s) remaining until deletion of files.\n")
    os.remove("master_key.csv")
    if os.path.exists("accounts_pass.csv"):
        os.remove("accounts_pass.csv")
    print("Access denied. Files deleted. You are welcome to create a new master key.")
    print("Shuting down...")
    sys.exit("Files deleted, restart the program...")


# geenkey = generate encryption key
def geenkey():
    key = Fernet.generate_key()
    keyring.set_password("passman", "encryption_key", key.decode())

# loenkey = load_encryption_key


def loenkey():
    key = keyring.get_password("passman", "encryption_key")
    return key.encode()

# encrypt the key


def encrypt_key(key, encryption_key):
    fernet = Fernet(encryption_key)
    return fernet.encrypt(key.encode()).decode()

# decrypts the key


def decrypt_key(encrypted_key, encryption_key):
    _ = Fernet(encryption_key)
    return _.decrypt(encrypted_key.encode()).decode()

# Function to save an encrypted password to a CSV file


def savepass(site_name, password):

    encryption_key = loenkey()

    encrypted_password = encrypt_key(password, encryption_key)

    password_dict = {}
    password_dict[site_name] = encrypted_password

    with open(accpss, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([site_name, encrypted_password])

    print(f"Password for {site_name} saved successfully!")
    return password_dict


def decrypt_and_print_passwords():
    data = []
    encryption_key = loenkey()
    fernet = Fernet(encryption_key)
    if os.path.exists("accounts_pass.csv") == False:
        print(("Can´t print. Password list doesn´t exist."))
        return
    with open(accpss, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            site = row[0]
            encrypted_password = row[1]
            decrypted_password = fernet.decrypt(encrypted_password.encode()).decode()
            data.append([site, decrypted_password])
    headers = ["Site", "Password"]
    print(tabulate(data, headers=headers, tablefmt="grid"))

    # prompt to go back to menu
    while True:
        x = input("Would you like to go back to the menu? (yes or no): ").strip().lower()
        if x in ("yes", "ye", "y"):
            return
        elif x in ("no", "n"):
            print("Exiting...")
            sys.exit(0)
        else:
            print("Please input only yes or no.")

#func to restores th epasswords when prompted by its username(now supports more than one username/site_name at the same time)
def restore_password():
    data = []
    encryption_key = loenkey()
    if os.path.exists("accounts_pass.csv") == False:
        print(("Can´t print. Password list doesn´t exist."))
        return

    filter_by = input("Enter the site or username associated with the password you want to restore): ").strip().lower()
    with open(accpss, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            site = row[0]
            encrypted_password = row[1]
            if filter_by and filter_by.lower() not in site.lower():
                continue
            decrypted_password = decrypt_key(encrypted_password, encryption_key)
            data.append([site, decrypted_password])
    headers = ["Site", "Password"]
    print(tabulate(data, headers=headers, tablefmt="grid"))

    # Prompt to go back to menu
    while True:
        x = input("Would you like to go back to the menu? (yes or no): ").strip().lower()
        if x in ("yes", "ye", "y"):
            return
        elif x in ("no", "n"):
            print("Exiting...")
            sys.exit(0)
        else:
            print("Please input only yes or no.")


#function to add passwords
def add_password():
    encryption_key = loenkey()

    while True:
        while True:
            username = input("Enter the username or site name: ").strip()
            password = getpass.getpass("Enter the password: ").strip()
            if not username or not password:
                print("Username or password cannot be empty.")
            else:
                break

        encrypted_password = encrypt_key(password, encryption_key)
        with open(accpss, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, encrypted_password])
        print(f"Password for {username} saved successfully!")

        while True:
            x = input("Would you like to add another account? (yes or no): ").strip().lower()
            if x in ("yes", "ye", "y"):
                break
            elif x in ("no", "n"):
                print("Returning to main menu...\n")
                return
            else:
                print("Please input only yes or no.")

if __name__=="__main__":
    main()
