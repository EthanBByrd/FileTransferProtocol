# FileTransferProtocol

# Client File
This script is designed to operate as a client in a client-server model, using TCP (Transmission Control Protocol) for network communication. Here's a breakdown of its components and how it functions:

1. **Importing Required Module**: It starts by importing the `socket` module, which is necessary for any network communication.

2. **Setting Up Connection Parameters**:
   - `IP`: It obtains the host machine's IP address by using `socket.gethostbyname(socket.gethostname())`. This is intended to work on a local network where the client and server are on the same network segment.
   - `PORT`: Sets the port number to `4455`, which is the port on which the server is expected to listen for incoming connections.
   - `ADDR`: A tuple combining `IP` and `PORT` to specify the address of the server.
   - `FORMAT`: A string denoting the encoding format (`"utf-8"`) to be used for sending and receiving data.
   - `SIZE`: Specifies the size (in bytes) of the buffer to be used when receiving data from the server, set to `1024`.

3. **The `main` Function**: This function encapsulates the client's workflow.
   - **Starting a TCP Socket**: It creates a new socket object with `AF_INET` (IPv4) and `SOCK_STREAM` (TCP) as parameters, establishing a TCP connection.
   - **Connecting to the Server**: The client attempts to connect to the server using the address specified by `ADDR`.
   - **File Handling**: It opens a file named `project.txt` for reading, presumably to send its contents to the server.
   - **Communicating File Name**: Sends the name of the file (`"project.txt"`) to the server, then waits for and prints a response from the server.
   - **Sending File Data**: Reads the contents of `project.txt`, sends this data to the server, awaits a response, and prints it.
   - **Resource Cleanup**: Closes the file and the connection to the server.

# Server File
This script sets up a server that listens for incoming TCP connections from clients. It is designed to receive a file name and file data from a client, save it, and then close the connection. Here's a detailed breakdown of its operation:

1. **Importing Required Module**: The script begins by importing the `socket` module, essential for network communication.

2. **Setting Up Connection Parameters**:
   - `IP`: Retrieves the host machine's IP address using `socket.gethostbyname(socket.gethostname())`, aiming for operations within a local network.
   - `PORT`: Specifies the port number (`4455`) on which the server listens for incoming connections.
   - `ADDR`: Combines `IP` and `PORT` into a tuple to define the server's address.
   - `SIZE`: Sets the buffer size to `1024` bytes for receiving data.
   - `FORMAT`: Defines `"utf-8"` as the encoding format for data transmission.

3. **The `main` Function**: Outlines the server's workflow.
   - **Server Initialization**: Displays a starting message and initializes a TCP socket with `AF_INET` (IPv4) and `SOCK_STREAM` (TCP) parameters.
   - **Binding to the Server**: Binds the IP address and port number to the server socket.
   - **Listening for Connections**: The server starts listening for client connections, indicating it's ready to accept connections.
   - **Handling Client Connections**: Uses a loop to continuously accept new connections. For each connection:
     - Accepts a connection from a client and prints the address of the connected client.
     - Receives the name of a file from the client, creates/opens the file in write mode, and sends a confirmation back to the client.
     - Receives file data from the client, writes it to the file, sends a confirmation that the data was received, and then closes the file.
     - Closes the connection with the client and prints a message indicating the client has been disconnected.

The server remains in the listening state, ready to accept new connections until the script is manually terminated.

