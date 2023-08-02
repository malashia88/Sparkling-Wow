
def write_user_data(filename):
    # Prompt the user for input
    name = input("Enter your name: ")
    address = input("Enter your street address: ")
    phone_number = input("Enter your phone number: ")

    # Write the user data to the file
    with open(filename, "w") as file:
        file.write(f"{name},{address},{phone_number}\n")

    print("User data has been written to the file.")

def read_file_contents(filename):
    # Read the file and display its contents
    with open(filename, "r") as file:
        contents = file.read()

    print("File contents:")
    print(contents)

# Prompt the user for the file name
file_name = input("Enter the file name: ")

# Write user data to the file
write_user_data(file_name)

# Read and display the file contents
read_file_contents(file_name)