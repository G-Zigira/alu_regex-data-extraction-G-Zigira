# 📄 Text Scanning Threat Detector (Python)

## 📌 Project Description
This project is a Python program that scans a text file for potentially malicious or suspicious patterns such as:
- SQL Injection attempts  
- Cross-Site Scripting (XSS) patterns  
- Dangerous keywords (e.g. DROP, DELETE, SELECT, etc.)

It reads input from a text file and reports any detected threats.

---

## 🛠 Requirements
- Python 3.x  
- No external libraries required (uses built-in Python modules only)

---

## 📂 Project Structure
project-folder/
│
├── main.py
├── dummyinput.txt
└── README.md

---

## ▶️ How to Run the Program

1. Open a terminal in the project folder.
2. Run the program using: Scanner_main.py

The program will scan the contents of `dummyinput.txt` and display any detected threats.

---

## 🔁 Replacing the Input File

The program is designed to always read from a file named: `dummyinput.txt`

### To scan a different file:

1. Delete or remove the existing `dummyinput.txt` file.
2. Delete any exofile with results if any.
3. Add your new text file into the project folder.
4. Rename your new file to: `dummyinput.txt`
5. Run the program again:

⚠️ **Important:**  
The filename must be `dummyinput.txt` or the program will not work unless you change the filename in the code.

---


