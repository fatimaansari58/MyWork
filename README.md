# COURSE PROJECT
# Text Encryptor & Decryptor (Streamlit Application)

## Overview

This project is a Python-based web application that allows users to protect their text messages through encryption and retrieve them through decryption.
It uses the Fernet symmetric encryption technique and provides an easy-to-use interface built with Streamlit.

The application is designed to help beginners understand how basic cryptography can be implemented in real-world applications.


## Developer

 Fatima Ansari
--- 
## Project Functionality

* Generates a secure random encryption key
* Accepts a user-provided secret key
* Encrypts plain text into unreadable encrypted code
* Decrypts encrypted text back to its original form
* Uses tabs to separate encryption and decryption tasks
* Displays clear success, warning, and error messages

---

## How the Application Works

1. The user generates or enters a Fernet secret key.
2. Using the provided key, the system initializes the encryption engine.
3. In the encryption section, the user enters plain text and converts it into encrypted form.
4. In the decryption section, the encrypted text is decoded back into readable text using the same key.
5. If the key or encrypted text is incorrect, the application displays an error message.

---

## Technologies and Libraries

* Python
* Streamlit (for web interface)
* Cryptography library (Fernet encryption)

---

## Security Note

The same secret key must be used for both encryption and decryption.
If the key is lost or incorrect, the encrypted message cannot be recovered.

---

## Steps to Run the Project

1. Ensure Python is installed on your system.
2. Install required libraries using the following commands:
   pip install streamlit cryptography
3. Save the Python file (for example: text_encryptor.py).
4. Open a terminal in the project directory.
5. Run the application with:
   streamlit run text_encryptor.py
6. The app will launch in your default web browser.

---

## Educational Purpose

This project is created for academic and learning purposes.
It demonstrates:

* Basic use of cryptographic concepts
* Secure handling of user input
* Implementation of symmetric encryption
* Development of interactive Python web apps

---

## Usage License


This project is intended for educational use and practice purposes only.


 ----

 
 # Standalone App which runs only on desktop interface
# Fernet Encryption & Decryption GUI (Python Tkinter)

## Project Summary

This project is a desktop-based encryption and decryption application developed using Python.
It provides a graphical user interface (GUI) that allows users to securely convert readable text into encrypted form and then restore it back using symmetric key cryptography.

The application is built with Tkinter for the interface and uses the Fernet algorithm from the Cryptography library for secure data handling.

---

## Author

 Fatima Ansari

---

## Main Features

* Desktop graphical user interface using Tkinter
* Automatic generation of a symmetric encryption key
* Encryption of user-entered plain text
* Decryption of encrypted text using the same key
* Alert messages for empty input or invalid data
* Simple and beginner-friendly design

---

## How the Application Works

1. A secure Fernet key is generated when the program starts.
2. The user enters text into the input area.
3. Clicking the "Encrypt" button converts the text into encrypted format.
4. Clicking the "Decrypt" button restores encrypted text to its original form.
5. Error messages are shown if the input is invalid or cannot be decrypted.

---

## Technologies Used

* Python
* Tkinter (GUI development)
* Cryptography library (Fernet symmetric encryption)

---

## How to Run the Program

1. Ensure Python is installed on your system.
2. Install the required library using the command:
   pip install cryptography
3. Save the Python file (for example: fernet_gui.py).
4. Run the program using:
   python fernet_gui.py

---

## Purpose of the Project

This project is created for educational purposes to help students understand:

* Basic concepts of encryption and decryption
* Symmetric key cryptography
* GUI development using Tkinter
* Secure handling of text data in Python

---

## Limitations

* The encryption key is generated at runtime and not stored permanently.
* Encrypted data cannot be decrypted after restarting the application.

---

## License

This project is intended for academic and learning use only.

