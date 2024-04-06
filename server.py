import socket
import ssl
import time
import os

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"


def main():
    print("[STARTING] Server is starting.")

    # Setting up SSL context
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="server.crt", keyfile="server.key")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(ADDR)
        server.listen()
        print("[LISTENING] Server is listening.")

        while True:
            conn, addr = server.accept()
            with context.wrap_socket(conn, server_side=True) as sconn:
                print(f"[NEW CONNECTION] {addr} connected.")

                start_time = time.time()

                # Receiving the filename
                filename = sconn.recv(SIZE).decode(FORMAT)
                print(f"[RECV] Receiving the filename.")
                with open("server_data/" + filename, "w") as file:
                    sconn.send("Filename received.".encode(FORMAT))

                    # Handle invalid filename case """
                    filename = os.path.basename(filename)
                    if not filename:
                        """ Handle invalid filename case """
                        conn.send("Invalid filename".encode(FORMAT))
                        conn.close()
                        continue

                    # Receiving the file data
                    data = sconn.recv(SIZE).decode(FORMAT)
                    print(f"[RECV] Receiving the file data.")
                    file.write(data)
                    sconn.send("File data received.".encode(FORMAT))

                end_time = time.time()
                print(f"File received and saved in {end_time - start_time} seconds.")

                print(f"[DISCONNECTED] {addr} disconnected.")


if __name__ == "__main__":
    main()
