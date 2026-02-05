Text Scanning Threat Detector (Python)
Project Description

This project is a Python program that scans a text file for potentially malicious or suspicious patterns such as:

SQL Injection attempts

Cross-Site Scripting (XSS) patterns

Dangerous keywords (e.g. DROP, DELETE, SELECT, etc.)

It reads input from a text file and reports any detected threats.

🛠 Requirements

Python 3.x

No external libraries required (uses built-in Python modules only)

Project Structure
project-folder/
│
├── main.py
├── dummyinput.txt
└── README.md

How to Run the Program

Open a terminal in the project folder.

Run the program using:

python main.py


The program will scan the contents of dummyinput.txt and display any detected threats.

Replacing the Input File

The program is designed to always read from a file named:

dummyinput.txt

To scan a different file:

Delete or remove the existing dummyinput.txt file.

Add your new text file into the project folder.

Rename your new file to:

dummyinput.txt


Run the program again:

python main.py


Important:
The filename must be dummyinput.txt or the program will not work unless you change the filename in the code.


Purpose

This project demonstrates:

File handling in Python

Pattern matching using regular expressions

Basic cybersecurity threat detection concepts