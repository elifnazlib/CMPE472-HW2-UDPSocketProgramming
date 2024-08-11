import socket

def start_server():
    permitted_numbers = []
    ports = []
    num_clients = 0

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 1212)) 

    while num_clients < 4:
        data, address = server_socket.recvfrom(4096)

        client_port = address[1]
        message = data.decode()

        print(f"Message:    {message}")
        print(f"Client Address:   {address}")

        if client_port in ports: 
            num_clients = num_clients
        else:
            ports.append(client_port)
            num_clients += 1
 
        if client_port  == 1234:
            number = message[10:]
            if "Permission".casefold()  == message[0:10].casefold() and len(message)  > 10 and not " " in message and number.isdigit():
                if number in permitted_numbers:
                    response = "Already Permitted"
                else:
                    permitted_numbers.append(number)
                    response = "Permission Accepted"
            else:
                response = "Invalid Message"    
        elif client_port  == 3333:
            number = message[7:]
            if "Request".casefold()  == message[0:7].casefold() and len(message)  > 7 and not " " in message and number.isdigit():
                if number in permitted_numbers:
                    response = "Request Accepted"
                else:
                    response = "Request Rejected"
            else:
                response = "Invalid Message"
        else:
            response = "Port is not allowed to communicate"

        server_socket.sendto(response.encode(), address)

    if num_clients == 4:
        print(f"The number of connected clients is: ", num_clients)

if __name__ == "__main__":
    start_server()