import random
import string
import mysql.connector
from mysql.connector import Error

MAX_PASSWORD_LENGTH = 50

def generate_password(length, use_symbols, use_numbers, use_uppercase, use_lowercase, db_config, table, value_name):
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
        if not password_exists(password, db_config, table, value_name):
            add_password_to_db(password, db_config, table, value_name)
            break
        else:
            print("Password already exists, generating a new one...")

    return password

def password_exists(password, db_config, table, value_name):
    try:
        with mysql.connector.connect(**db_config) as conn:
            cursor = conn.cursor()
            query = f"SELECT 1 FROM {table} WHERE {value_name} = %s"
            cursor.execute(query, (password,))
            return cursor.fetchone() is not None
    except Error as e:
        print(f"Error: {e}")
        return False

def add_password_to_db(password, db_config, table, value_name):
    try:
        with mysql.connector.connect(**db_config) as conn:
            cursor = conn.cursor()
            query = f"INSERT INTO {table} ({value_name}) VALUES (%s)"
            cursor.execute(query, (password,))
            conn.commit()
            print("Password added to database")
    except Error as e:
        print(f"Error: {e}")

def main():
    db_config = {}
    db_config['host'] = input("Enter the database host: ")
    db_config['user'] = input("Enter the database username: ")
    db_config['password'] = input("Enter the database password: ")
    db_config['database'] = input("Enter the database name: ")
    table = input("Enter the table name: ")
    value_name = input("Enter the value name to check against: ")

    try:
        mysql.connector.connect(**db_config).close()
    except Error as e:
        print(f"Error: {e}")
        return

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

            password = generate_password(length, use_symbols, use_numbers, use_uppercase, use_lowercase, db_config, table, value_name)
            print(f"Generated password: {password}")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
