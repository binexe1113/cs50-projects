    # PASSMAN
    #### Video Demo: https://www.youtube.com/watch?v=onKPhPLwAc8
    #### Description:
Passman is a password manager that uses a combination of cryptography and comma-separated values to allow the user to either generate a password,
Restore a password, add an existing password, or just check the list containing every single password inputed on it and its username/site associated with since the user correctly inputs or defines the master key.
    A master key is a password prompt to the user in his first run of the program; it uses the getpass library to hide user input while he types (every password prompt uses the getpass for privacy). then the program cryptographs the
key and stores it in a.csv file. After re-opening the program, the user gets prompted for the master key; if he fails five times, the OS library is used to delete the file containing the master key and the file containing passwords for accounts.
    If the user prompts the correct key, the menu shows itself, allowing the user to choose between a series of functions already mentioned above. To generate a password, Passman uses a combination of the string library (python native) to extrapolate.
already existing lists, including ascii_letters, punctuation, and digits; it then concatenates these three lists into one and, using user input for its length, extracts random elements from this list using the random.choice method from the random library.
(also native to Python); furthermore, the generating a random password function then shows the user the created password and prompts for a yes or no question regarding the storage (or not) of the password in question.
    If the user so chooses, it can store that password after prompting the user for a site/username to associate with.
To store the account, the code activates the savepass (save password) function. savepass takes two arguments, the site_name (or username) and the password. The password is then encrypted using the cryptography library (using Fernet) and storing the key used for it in a keyring (using the keyring library).
    The user can also restore a password if he so chooses from the menu. It asks the user for input (that is, the site/username associated with the password it wishes to retrieve), and with a simple loop, it scans through the whole account. csv file looking for the user input,
then using the tabulate library prints a good-looking table with every corresponding username/site and the passwords (decrypted) associated with it.
    Also, the user can add an existing account to the.csv file. The program will prompt the user to input the username and the password, then encrypt the password and write it into the.csv file (using the csv library) and save it.
    The last option the user has is to print all the existing sites and the decrypted passwords associated with them using again fernet to decrypt, keyring to access the encryption key, csv.reader to read the file, and tabulate to print in beautifully.
And this is PASSMAN.
