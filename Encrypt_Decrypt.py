# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 16:01:50 2026

@author: Fatima Ansari
"""

import streamlit as st
from cryptography.fernet import Fernet

st.title("🔐 Text Encryptor & Decryptor")
st.write("Secure your messages using Fernet symmetric encryption.")
st.write("A project developed by: **Fatima Ansari**")
# --- STEP 1: Key Management ---
st.subheader("1. Your Secret Key")

# Helper function to generate a new key
if st.button("Generate New Random Key"):
    new_key = Fernet.generate_key().decode()
    st.code(new_key, language="text")
    st.info("Copy this key! You need it to decrypt your message later.")

# Input field for the key
key_input = st.text_input("Enter your 32-byte Fernet key:", type="password")

# --- STEP 2: Encryption & Decryption Logic ---
if key_input:
    try:
        # Initialize the Fernet object with the user's key
        cipher_suite = Fernet(key_input.encode())

        # Create two tabs for a cleaner UI
        tab1, tab2 = st.tabs(["Encrypt Text", "Decrypt Text"])

        with tab1:
            text_to_encrypt = st.text_area("Message to hide:")
            if st.button("Encrypt"):
                if text_to_encrypt:
                    # Encrypt the text
                    encoded_text = text_to_encrypt.encode()
                    encrypted_text = cipher_suite.encrypt(encoded_text)
                    st.success("Message Encrypted!")
                    st.code(encrypted_text.decode(), language="text")
                else:
                    st.warning("Please enter some text.")

        with tab2:
            text_to_decrypt = st.text_area("Encrypted code to reveal:")
            if st.button("Decrypt"):
                if text_to_decrypt:
                    try:
                        # Decrypt the text
                        decrypted_text = cipher_suite.decrypt(text_to_decrypt.encode())
                        st.success("Message Decrypted!")
                        st.write(f"**Result:** {decrypted_text.decode()}")
                    except Exception:
                        st.error("Decryption failed. Ensure the key and code are correct.")
                else:
                    st.warning("Please enter the encrypted text.")
                    
    except ValueError:
        st.error("Invalid Key! A Fernet key must be 32 url-safe base64-encoded bytes.")

else:
    st.info("Please enter or generate a key to start.")