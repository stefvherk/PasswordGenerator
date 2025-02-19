# PasswordGenerator

PasswordGenerator is a Python application that generates secure passwords based on user preferences and ensures the generated passwords are unique by storing them in a MySQL database.

## Features

- Generate passwords with customizable length.
- Include or exclude symbols, numbers, uppercase, and lowercase letters.
- Ensure generated passwords are unique by checking against a MySQL database.

## Requirements

- Python 3.x
- MySQL server
- `mysql-connector-python` package

## Installation

1. Clone the repository or download the source code.
2. Install the required Python package:
    ```sh
    pip install mysql-connector-python
    ```
3. Set up your MySQL database and create a table to store passwords:

## Configuration

The script will prompt you to enter your MySQL database connection details, table name, and the column name to check against.

## Usage

Run the `gen.py` script:
```sh
python gen.py
```

Follow the prompts to generate a password based on your preferences. The generated password will be displayed and stored in the database if it is unique.
