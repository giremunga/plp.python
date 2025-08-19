def file_read_write():
    # Ask the user for a filename
    filename = input("Enter the name of the file to read: ")

    try:
        # Try to open and read the file
        with open(filename, "r") as file:
            content = file.read()

        # Modify the content
        modified_content = content.upper()

        # Create a new file to write the modified content
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f" File '{filename}' was read successfully.")
        print(f"Modified content has been written to '{new_filename}'.")

    except FileNotFoundError:
        print(f" Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f" Error: You don’t have permission to read '{filename}'.")
    except Exception as e:
        print(f" An unexpected error occurred: {e}")


# Run 
file_read_write()
