import shutil  # Import the shutil module for file operations
import os      # Import the os module for operating system functions
import tkinter as tk  # Import the tkinter library for creating a GUI
from tkinter import filedialog  # Import the filedialog module from tkinter

# Define a function to copy and rename files
def copy_and_rename_files(input_path, output_directory, num_copies):
    # Split the input path to get the file name and extension
    file_name, file_extension = os.path.splitext(os.path.basename(input_path))

    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Loop to create the specified number of copies
    for counter in range(1, num_copies + 1):
        # Create the new file name with the incremented counter
        new_file_name = f'{file_name} copy {counter}{file_extension}'

        # Construct the full output path by joining the directory and new filename
        output_path = os.path.join(output_directory, new_file_name)

        # Copy the file from the input path to the output path
        shutil.copy(input_path, output_path)

# Define the main function
def main():
    root = tk.Tk()  # Create a tkinter root window
    root.withdraw()  # Hide the main window (we only need the file dialog)

    # Ask the user to select the input file using a file dialog
    input_file_path = filedialog.askopenfilename(title="Select a file to copy")

    if not input_file_path:
        print("No file selected. Exiting.")
        return

    # Set the output directory to "Output Copies"
    output_directory = "Output Copies"

    try:
        # Ask the user to enter the number of copies to make
        num_copies = int(input("Enter the number of copies to make: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    else:
        # Call the copy_and_rename_files function with the input file, output directory, and num_copies
        copy_and_rename_files(input_file_path, output_directory, num_copies)
        print(f"Copies of {input_file_path} have been created in {output_directory}.")

# Check if this script is the main program
if __name__ == "__main__":
    main()  # Call the main function if this script is executed directly
