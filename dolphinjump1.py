import os
import time

def dolphinjump():
    """A simple text-based operating system called Dolphinjump."""

    def clear_screen():
        """Clears the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_help():
        """Displays available commands."""
        print("Available commands:")
        print("  help      - Display this help message")
        print("  clear     - Clear the screen")
        print("  echo <text> - Display the given text")
        print("  date      - Display the current date and time")
        print("  exit      - Exit Dolphinjump")
        print("  calc <expression> - Evaluates a simple mathematical expression")
        print("  list <directory> - Lists files in the specified directory.")
        print("  create <filename> - Creates an empty file.")
        print("  read <filename> - Reads the content of a file.")
        print("  write <filename> <text> - Writes text to a file.")

    def display_date():
        """Displays the current date and time."""
        print(time.strftime("%Y-%m-%d %H:%M:%S"))

    def echo(text):
        """Displays the given text."""
        print(text)

    def calculate(expression):
        """Evaluates a simple mathematical expression."""
        try:
            result = eval(expression)
            print(result)
        except (SyntaxError, NameError, TypeError, ZeroDivisionError):
            print("Invalid expression.")

    def list_files(directory):
        """Lists files in the specified directory."""
        try:
            files = os.listdir(directory)
            for file in files:
                print(file)
        except FileNotFoundError:
            print(f"Directory '{directory}' not found.")
        except NotADirectoryError:
            print(f"'{directory}' is not a directory.")

    def create_file(filename):
        """Creates an empty file."""
        try:
            with open(filename, 'w'):
                pass  # Create an empty file
            print(f"File '{filename}' created.")
        except Exception as e:
            print(f"Error creating file: {e}")

    def read_file(filename):
        """Reads the content of a file."""
        try:
            with open(filename, 'r') as f:
                content = f.read()
                print(content)
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except Exception as e:
            print(f"Error reading file: {e}")

    def write_file(filename, text):
        """Writes text to a file."""
        try:
            with open(filename, 'w') as f:
                f.write(text)
            print(f"Text written to '{filename}'.")
        except Exception as e:
            print(f"Error writing to file: {e}")

    clear_screen()
    print("Welcome to Dolphinjump!")
    display_help()

    while True:
        command = input("Dolphinjump> ").strip()
        parts = command.split(' ', 1)
        action = parts[0].lower()
        arguments = parts[1] if len(parts) > 1 else ''

        if action == 'help':
            display_help()
        elif action == 'clear':
            clear_screen()
        elif action == 'echo':
            echo(arguments)
        elif action == 'date':
            display_date()
        elif action == 'exit':
            print("Exiting Dolphinjump...")
            break
        elif action == 'calc':
            calculate(arguments)
        elif action == 'list':
            list_files(arguments or '.')
        elif action == 'create':
            create_file(arguments)
        elif action == 'read':
            read_file(arguments)
        elif action == 'write':
            parts_write = arguments.split(' ', 1)
            if len(parts_write) == 2:
                write_file(parts_write[0], parts_write[1])
            else:
                print("Usage: write <filename> <text>")
        elif action:
            print(f"Unknown command: {action}")

if __name__ == "__main__":
    dolphinjump()
