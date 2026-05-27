# filehandlingsystem.py

Project Title

File Handling System using Python(Note-Taking / Log Management)-

Description

This project demonstrates Python File Handling operations using a menu-driven interface. The system allows users to create, read, append, update, and delete text files.

Technologies Used-

Python 3
File I/O Operations
Exception Handling
Concepts Covered

open() function
File modes: 'r', 'w', 'a', 'r+'
Exception handling
Functions
Loops
Menu-driven programs
Edge Cases Tested

Empty files
Non-existing files
Invalid line numbers
Large files
Special characters
How to Run

Save the code in a file named file_system.py
Open terminal or command prompt
Run:
python file_system.py

Explanation of File Modes

Mode	Purpose
'r'	Read file
'w'	Write file (overwrite)
'a'	Append content
'r+'	Read and write

Features Included-

Create a new file
Read file content
Append text to file
Update specific lines
Delete file
Error handling using try-except
Menu-driven interface
Uses Python file modes: 'r', 'w', 'a', 'r+'
Uses with statement for safe file handling

Sample Input / Output-

Example 1: Create File

===== FILE HANDLING SYSTEM =====

1. Create New File
2. Read File
3. Append Text
4. Update Specific Line
5. Delete File
6. Exit

Enter your choice: 1
Enter file name: notes.txt
Enter content for the file:
Hello World

File created successfully.

Example 2: Read File

Enter your choice: 2
Enter file name to read: notes.txt

File Content:
Hello World

Example 3: Append Text

Enter your choice: 3
Enter file name to append text: notes.txt
Enter text to append:
This is second line.

Text appended successfully.

Example 4: Update Line

Enter your choice: 4
Enter file name to update: notes.txt

Current File Content:
1. Hello World
2. This is second line.

Enter line number to update: 2
Enter new text: Updated second line

Line updated successfully.

Example 5: Delete File

Enter your choice: 5
Enter file name to delete: notes.txt

File deleted successfully.

