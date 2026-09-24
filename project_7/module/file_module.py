def new_file():
    try:
        file_name = input("Enter File name: ")
        
        with open(file_name, "x"):
            pass
        
        print("File created successfully!")

    except FileExistsError:
        print("Error: File already exists!")
def write_file():
    try:
        f_name = input("Enter File name: ")
        data = input("Enter data to Write: ")

        with open(f_name, "w") as file:
            file.write(data)

        print("Data written successfully!")

    except FileNotFoundError:
        print("Error: File not found!")

def read_file():
    try:
        f_name = input("Enter file name: ")

        with open(f_name, "r") as file:
            content = file.read()

        print("File Content:")
        print(content)

    except FileNotFoundError:
        print("Error: File not found!")

def append_file():
    try:
        f_name = input("Enter File name: ")
        data = input("Enter data to append: ")

        with open(f_name, "a") as file:
            file.write(data)

        print("Data Append successfully!")

    except FileNotFoundError:
        print("Error: File not found!")
