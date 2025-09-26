import socket

def modString(s: str) -> str:
    reversedMsg = s[::-1]
    swappedMsg = reversedMsg.swapcase()

    return swappedMsg

def server():
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    server_binding = ('', 30038)
    ss.bind(server_binding)
    ss.listen(1)
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))
    csockid, addr = ss.accept()
    print ("[S]: Got a connection request from a client at {}".format(addr))

    # send a intro message to the client.  
    msg = "Welcome to CS 352!"
    csockid.send(msg.encode('utf-8'))

    # Receive message from client
    client_msg = csockid.recv(100).decode('utf-8')
    print(f'[S]: got a message from client {client_msg}')

    # Send modified message back to client
    modified_msg = modString(client_msg)
    csockid.send(modified_msg.encode("utf-8"))
    print("[S]: sent modified message back to client")

    # Close the server socket
    ss.close()
    exit()

if __name__ == "__main__":
    server()