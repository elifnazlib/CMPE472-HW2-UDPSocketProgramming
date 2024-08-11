# CMPE 472 – Computer Networks - Programming Assignment 2

#### Topic: UDP Socket Programming
In this assignment, you must build a mini application using UDP socket programming.

#### The requirements are as follows:
- You will use UDP sockets in this assignment.
- The sockets will belong to the same host. In other words, you will use localhost communication.

## Client side:
- The port of the client side socket will be determined by user. The client side program will ask the user to define a port number.
- After creation of the socket, the program will ask the user to enter a message. Then, the message will be sent to the server. Then, the server’s response will be read and printed on the screen.
- If the server sends “Port is not allowed to communicate” as a response, the client socket will be closed and the client side program will be finished.
- You must have only one client.py file. Do not write different files for client sockets with different ports. You have to handle all of them in one file.

## Server side:
- The server will receive messages from the clients. If the total numbers of clients which has sent a message to the server is greater than or equal to 4, close the server socket and finish the server side program.
- The server will keep track of numbers which are permitted. You can use an array or list for this purpose.
- After receiving a message, the server will print the received message and the address of the client (IP address and port number).
* If the port of the client is 1234:
  - The messages have to start with the text “Permission” and end with a number (“Permission1111”, “pErMission33”, “permission3”, etc.). If the message is not in this format, the server socket has to send “Invalid Message” message to the client.
  - The number following the “Permission” will be extracted. This number will be added to list of permitted numbers. In this case, “Permission Accepted” message will be send to the client.
  - If the number is already in the list (it was permitted before), “Already Permitted” message will be send to the client.
* If the port of the client is 3333:
  - The messages have to start with the text “Request” and end with a number (“Request1111”, “requEST33”, “request3”, etc.). If the message is not in this format, the server socket has to send “Invalid Message” message to the client.
  - The number following the “Request” will be extracted. If the number is already in the list of permitted numbers, “Request Accepted” message will be sent to the client. If it is not in the list, “Request Rejected” message will be sent to the client.
* If the port of the client is not 1234 or 3333:
  - The response of the server will be "Port is not allowed to communicate" regardless of the content of the message.


<br> 

*** 


#### Output:
<img width="1440" alt="output" src="https://github.com/user-attachments/assets/f4d9f74c-3db6-45d3-bef3-4aad8e4fa2b1">

<br> 
<br>
<br>

## Developers:
[Büşra Ekici](https://github.com/busraekicii) <br>
[Elif Nazlı Böke](https://github.com/elifnazlib) <br>
[Gülce Ayşe Döker](https://github.com/GulceAyseDoker)
