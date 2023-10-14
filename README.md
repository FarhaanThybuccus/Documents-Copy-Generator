# Documents-Copy-Generator
This Python script provides a simple graphical user interface (GUI) for selecting a source file and making multiple copies of that file while renaming them. It allows you to specify the number of copies you want to create. The script uses the shutil and os libraries for file operations and the tkinter library for creating the user interface.

Features:
Select a source file to be copied and renamed using a user-friendly file dialog.
Specify the number of copies to create.
Copies of the source file are placed in an output directory, and each copy is given a unique name to differentiate it from the original.

How to Use:
Run the script, and a simple GUI window will appear.
Click the "Select a file to copy" button to choose the source file.
Enter the desired number of copies you want to create.
The copies will be placed in an "Output Copies" directory in the same location as the script.

Dependencies:
Python 3.x
tkinter: This library comes pre-installed with most Python distributions and is used for creating the file dialog for selecting the source file.
shutil: This library is used for file copying.
os: This library is used for directory and file path operations.

Usage:
Clone or download this repository.
Make sure you have Python installed on your system.
Run the script by executing it from the command line or an integrated development environment (IDE).

Example:
Suppose you have a file named "example.txt" that you want to copy five times. Using this script, you can select "example.txt," enter "5" for the number of copies, and it will create five copies with distinct names, such as "example copy 1.txt," "example copy 2.txt," and so on, all placed in an "Output Copies" directory.

Contributions:
Contributions, bug reports, and feature requests are welcome. Feel free to open an issue or submit a pull request.
