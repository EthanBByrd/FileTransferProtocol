import socket
import ssl
import time

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024


def main():
    # Create a default SSL context
    context = ssl.create_default_context()

    # WARNING: This is insecure and should only be used for testing purposes
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    with socket.create_connection(ADDR) as sock:
        with context.wrap_socket(sock, server_hostname=IP) as ssock:
            print("[CONNECTED] Client connected to server securely.")

            file_path = "project.txt"  # Update this to the correct file path
            with open(file_path, "r") as file:
                data = file.read()

                start_time = time.time()

                # Sending the filename
                ssock.send("project.txt".encode(FORMAT))
                print(ssock.recv(SIZE).decode(FORMAT))

                # Sending the file data
                ssock.send(data.encode(FORMAT))
                print(ssock.recv(SIZE).decode(FORMAT))

                end_time = time.time()
                print(f"File transfer completed in {end_time - start_time} seconds.")


if __name__ == "__main__":
    main()
