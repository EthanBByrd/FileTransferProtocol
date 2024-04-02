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
   - **File Handling**: It opens a file named `yt.txt` for reading, presumably to send its contents to the server.
   - **Communicating File Name**: Sends the name of the file (`"yt.txt"`) to the server, then waits for and prints a response from the server.
   - **Sending File Data**: Reads the contents of `yt.txt`, sends this data to the server, awaits a response, and prints it.
   - **Resource Cleanup**: Closes the file and the connection to the server.
