import random
import string
import mysql.connector

MAX_PASSWORD_LENGTH = 50

def generate_password(length, use_symbols, use_numbers, use_uppercase, use_lowercase):
    if length > MAX_PASSWORD_LENGTH:
        raise ValueError(f"Password length cannot exceed {MAX_PASSWORD_LENGTH} characters")

    characters = ''.join([
        string.punctuation if use_symbols else '',
        string.digits if use_numbers else '',
        string.ascii_uppercase if use_uppercase else '',
        string.ascii_lowercase if use_lowercase else ''
    ])

    if not characters:
        raise ValueError("At least one character set must be selected")

    while True:
        password = ''.join(random.choice(characters) for _ in range(length))
        if not password_exists(password):
            add_password_to_db(password)
            break

    return password

def password_exists(password):
    with mysql.connector.connect(host="localhost", user="localuser", password="Trolkrongme3", database="userinfo") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM pass WHERE pass = %s", (password,))
        return cursor.fetchone() is not None

def add_password_to_db(password):
    with mysql.connector.connect(host="localhost", user="localuser", password="Trolkrongme3", database="userinfo") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pass (pass) VALUES (%s)", (password,))
        conn.commit()

def main():
    length = int(input(f"Enter the length of the password (max {MAX_PASSWORD_LENGTH}): "))
    if length > MAX_PASSWORD_LENGTH:
        raise ValueError(f"Password length cannot exceed {MAX_PASSWORD_LENGTH} characters")

    use_symbols = input("Use symbols? (yes/no): ").lower() == 'yes'
    use_numbers = input("Use numbers? (yes/no): ").lower() == 'yes'
    use_uppercase = input("Use uppercase letters? (yes/no): ").lower() == 'yes'
    use_lowercase = input("Use lowercase letters? (yes/no): ").lower() == 'yes'

    password = generate_password(length, use_symbols, use_numbers, use_uppercase, use_lowercase)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
