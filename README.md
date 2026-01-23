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
