# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("This is the first line of text\n")
        file.write("Second line with numbers: 12345\n")
        file.write("Third line with special characters: !@#$%\n")
except Exception as e:
    print("Error:", e)
finally:
    print("File creation completed.")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        print("Contents of my_file.txt:")
        print(file.read())
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print("Error:", e)

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Fourth line appended\n")
        file.write("Fifth line appended\n")
        file.write("Sixth line appended\n")
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print("Error:", e)
finally:
    print("File appending completed.")
