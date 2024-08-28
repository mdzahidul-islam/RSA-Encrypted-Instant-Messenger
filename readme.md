# Secure Instant Messenger (IM) with RSA

### Computer Network Security EECE 5850 (UML)

**Project Phase-2:** Integration of RSA into Secure Instant Messaging

**Submitted by:** Md Zahidul Islam and Parikshit Jadav 

## Project Overview

This project implements a Secure Instant Messenger (IM) using the RSA algorithm for encryption and decryption of messages. The goal is to ensure that only the intended recipient can decrypt and view the true content of the messages.

## Repository Contents

- `client1.py`
- `client2.py`
- `rsa.py`
- `server_.py`

## How to Run the Project

1. **Install Required Libraries:**
   Ensure Python 3 is installed with the following libraries: `tkinter`, `random`, `socket`.

2. **Run the Server:**
   Open a terminal, navigate to the project directory, and start the server with:
 
   python server_.py
   If needed, you can also try:
   python3 server_.py

3. **Start the Clients:**
   Open another terminal in the same directory and run:
   python client1.py
   Follow the prompts, pressing Enter twice to skip the host and port input if running locally.
   Repeat the same steps for client2.py in a separate terminal window.
4. **Using the Messenger:**
   The GUI will prompt you to enter a client name in the format "Client:Name".
   Start chatting securely!

## Key Management Note
The client1.py and client2.py files contain pre-generated public and private keys. Public keys are exchanged and stored manually to simulate a real-world Public Key Infrastructure (PKI) setup. This simplifies the code while reflecting the typical use of RSA in secure communications. The keys were generated using rsa.py with unique pairs of prime numbers.

