# FileTransferProtocol

## Overview
This project demonstrates the implementation of a secure file transfer system using Python's `socket` and `ssl` libraries, showcasing encrypted data transmission between a client and a server over a network.

## Client File

The client script is responsible for initiating a secure connection to the server and transmitting a specified file's contents. Here's a detailed breakdown of its functionality:

- **Importing Required Modules**: Utilizes the `socket`, `ssl`, and `time` modules for network communication and encryption.
- **Setting Up Connection Parameters**:
  - **IP**: Determines the host machine's IP address to facilitate communication over a local network.
  - **PORT**: Designates port number `4455`, which the server listens on for incoming connections.
  - **ADDR**: A tuple that combines `IP` and `PORT` to specify the server's network address.
  - **FORMAT**: Specifies `"utf-8"` encoding for data transmission.
  - **SIZE**: Defines the buffer size for data reception, set to `1024` bytes.
- **Main Functionality**:
  - Initiates a TCP socket and establishes a secure connection to the server.
  - Handles file operations for reading the contents of `project.txt` and transmits this data to the server.
  - Manages communication to send the file name and data to the server and prints server responses.

## Server File

The server script sets up a listening service that accepts encrypted file transmissions from clients, saving received files appropriately. Detailed operation includes:

- **Importing Required Modules**: Incorporates `socket`, `ssl`, `time`, and `os` modules for networking, encryption, and file management.
- **Setting Up Connection Parameters**:
  - Similar to the client, with additions for SSL context setup using a certificate (`server.crt`) and a private key (`server.key`).
- **Main Functionality**:
  - Initializes a server socket that binds to the specified IP address and port, then listens for incoming connections.
  - Accepts connections, securely wraps them using SSL, and processes received file name and data to save on the server.
  - Provides feedback to the client and handles multiple client connections in a loop.

## Security Note

The implementation, as designed, skips hostname verification and certificate validation for SSL connections, which is intended for demonstration and testing purposes only. For real-world applications, proper SSL certificate handling and verification mechanisms should be implemented.

## Running the Project

1. **Server Setup**: Start the server script first to ensure it's ready to accept connections:
   ```bash
   python Server.py


