import random
import string

def generate_password(length, use_symbols, use_numbers, use_uppercase, use_lowercase):
    characters = ""
    if use_symbols:
        characters += string.punctuation
    if use_numbers:
        characters += string.digits
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase

    if not characters:
        raise ValueError("At least one character set must be selected")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length = int(input("Enter the length of the password: "))
    use_symbols = input("Use symbols? (yes/no): ").lower() == 'yes'
    use_numbers = input("Use numbers? (yes/no): ").lower() == 'yes'
    use_uppercase = input("Use uppercase letters? (yes/no): ").lower() == 'yes'
    use_lowercase = input("Use lowercase letters? (yes/no): ").lower() == 'yes'

    password = generate_password(length, use_symbols, use_numbers, use_uppercase, use_lowercase)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()