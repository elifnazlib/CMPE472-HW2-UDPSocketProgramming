import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 1212)  

    port = int(input("Enter port no:"))
    client_socket.bind(('localhost', port))

    while True:
        message = input("Enter a message: ")
        client_socket.sendto(message.encode(), server_address)

        data, server = client_socket.recvfrom(4096)
        print(f"{data.decode()}")

        if "Port is not allowed to communicate" in data.decode():
            break
    client_socket.close()

if __name__ == "__main__":
    start_client()

