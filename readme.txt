## Computer Network Security EECE 5850 (UML)

Project phase-2: Secure Instant Messenger (IM) with RSA: Integration of IM with RSA

Submitted by: Parikshit Jadav and Md Zahidul Islam


This project is focused on implementing a Secure Instant Messenger with RSA algorithm. It focuses on integrating the RSA algorithm for the sender and receiver side for the encryption of the messages to be sent and received. This is to make sure that the actual receiver of the message get the true information.

The submission contains client1.py, client2.py, rsa.py and server_.py files. 

The steps to run the project are as follows:

1. Install the required python3 libraries: tkinter, random, socket etc.

2. Open a terminal window and change the directory to the codes directory.

3. Run following: "python server_.py". The server will keep running. (If it does not work, "python3 server_.py" command can also be used.)

4. Open another terminal at the same directory and run "python client1.py". Input as prompt in the terminal.
   Press Enter (2 times) to skip the host and port input to run in the same computer.

5. Similarly, run "python client2.py" in another terminal window and input as prompt.

6. The GUI will open. In the GUI, input client name as prompted ("Client:Name") and start chatting.

7. It's completed!

Note: The files client1.py and client2.py contains the public keys of each other and private keys of themselves. The code in these files does not generate the keys at the time of sending the message. This is done, to reduce the complexity of the code and to make the communication relatable to the real life encryption and decryption scenario, in which PKI has already announced the public keys of all the clients in the network and each client is aware about their own private key. The keys present in the files are generated using the unique pairs of prime numbers for each client by using rsa.py file.
