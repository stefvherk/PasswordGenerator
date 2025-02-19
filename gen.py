import random
import string
import mysql.connector

MAX_PASSWORD_LENGTH = 50

# Database connection details
DB_CONFIG = {
    'host': 'localhost',
    'user': 'localuser',
    'password': 'Trolkrongme3',
    'database': 'userinfo'
}

def generate_password(length, use_symbols, use_numbers, use_uppercase, use_lowercase):
    # Controleer of de lengte van het wachtwoord de maximale lengte overschrijdt
    if length > MAX_PASSWORD_LENGTH:
        raise ValueError(f"Password length cannot exceed {MAX_PASSWORD_LENGTH} characters")

    # Bouw de set van te gebruiken tekens op basis van de gebruikersvoorkeuren
    characters = ''.join([
        string.punctuation if use_symbols else '',
        string.digits if use_numbers else '',
        string.ascii_uppercase if use_uppercase else '',
        string.ascii_lowercase if use_lowercase else ''
    ])

    # Controleer of er ten minste één tekenreeks is geselecteerd
    if not characters:
        raise ValueError("At least one character set must be selected")

    # Genereer wachtwoorden totdat er een uniek wachtwoord is gevonden
    while True:
        password = ''.join(random.choice(characters) for _ in range(length))
        if not password_exists(password):
            add_password_to_db(password)
            break
        else:
            print("Password already exists, generating a new one...")

    return password

def password_exists(password):
    with mysql.connector.connect(**DB_CONFIG) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM pass WHERE pass = %s", (password,))
        return cursor.fetchone() is not None

def add_password_to_db(password):
    with mysql.connector.connect(**DB_CONFIG) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pass (pass) VALUES (%s)", (password,))
        conn.commit()
        print("Password added to database")

def main():
    while True:
        length_input = input(f"Enter the length of the password (max {MAX_PASSWORD_LENGTH}) or 'exit' to quit: ")
        if length_input.lower() == 'exit':
            break

        try:
            length = int(length_input)
            if length > MAX_PASSWORD_LENGTH:
                raise ValueError(f"Password length cannot exceed {MAX_PASSWORD_LENGTH} characters")

            use_symbols = input("Use symbols? (y/n): ").lower() == 'y'
            use_numbers = input("Use numbers? (y/n): ").lower() == 'y'
            use_uppercase = input("Use uppercase letters? (y/n): ").lower() == 'y'
            use_lowercase = input("Use lowercase letters? (y/n): ").lower() == 'y'

            password = generate_password(length, use_symbols, use_numbers, use_uppercase, use_lowercase)
            print(f"Generated password: {password}")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
