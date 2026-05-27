import os

# Function to create a new file
def create_file():
    filename = input("Enter file name: ")

    try:
        with open(filename, 'w') as file:
            content = input("Enter content for the file:\n")
            file.write(content + "\n")

        print("File created successfully.")

    except PermissionError:
        print("Permission denied.")


# Function to read file content
def read_file():
    filename = input("Enter file name to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()

            if content == "":
                print("File is empty.")
            else:
                print("\nFile Content:")
                print(content)

    except FileNotFoundError:
        print("File not found.")

    except PermissionError:
        print("Permission denied.")


# Function to append text to file
def append_file():
    filename = input("Enter file name to append text: ")

    try:
        with open(filename, 'a') as file:
            text = input("Enter text to append:\n")
            file.write(text + "\n")

        print("Text appended successfully.")

    except FileNotFoundError:
        print("File not found.")

    except PermissionError:
        print("Permission denied.")


# Function to update a specific line
def update_line():
    filename = input("Enter file name to update: ")

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        if len(lines) == 0:
            print("File is empty.")
            return

        print("\nCurrent File Content:")
        for i, line in enumerate(lines, start=1):
            print(f"{i}. {line.strip()}")

        line_number = int(input("Enter line number to update: "))

        if 1 <= line_number <= len(lines):
            new_text = input("Enter new text: ")
            lines[line_number - 1] = new_text + "\n"

            with open(filename, 'w') as file:
                file.writelines(lines)

            print("Line updated successfully.")

        else:
            print("Invalid line number.")

    except FileNotFoundError:
        print("File not found.")

    except PermissionError:
        print("Permission denied.")

    except ValueError:
        print("Please enter a valid number.")


# Function to delete a file
def delete_file():
    filename = input("Enter file name to delete: ")

    try:
        os.remove(filename)
        print("File deleted successfully.")

    except FileNotFoundError:
        print("File not found.")

    except PermissionError:
        print("Permission denied.")


# Main menu-driven program
def main():
    while True:
        print("\n===== FILE HANDLING SYSTEM =====")
        print("1. Create New File")
        print("2. Read File")
        print("3. Append Text")
        print("4. Update Specific Line")
        print("5. Delete File")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_file()

        elif choice == '2':
            read_file()

        elif choice == '3':
            append_file()

        elif choice == '4':
            update_line()

        elif choice == '5':
            delete_file()

        elif choice == '6':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the program
main()