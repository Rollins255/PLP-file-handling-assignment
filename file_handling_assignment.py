try:
    # File Creation
    with open("my_file.txt", "w") as file:
        file.write("Hello, this is line 1\n")
        file.write("12345, this is line 2\n")
        file.write("This is line 3, with numbers 67890\n")

    # File Reading and Display
    with open("my_file.txt", "r") as file:
        contents = file.read()
        print("Contents of the file after writing:")
        print(contents)

    # File Appending
    with open("my_file.txt", "a") as file:
        file.write("Appending this line 4\n")
        file.write("This is line 5, appended\n")
        file.write("Final appended line, with numbers 112233\n")

    # Read and Display after appending
    with open("my_file.txt", "r") as file:
        contents = file.read()
        print("Contents of the file after appending:")
        print(contents)

except FileNotFoundError as fnf_error:
    print(f"File not found error: {fnf_error}")
except PermissionError as perm_error:
    print(f"Permission error: {perm_error}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Execution completed.")
