import socket

def client():
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()
        
    # Define the port on which you want to connect to the server
    port = 30038
    localhost_addr = socket.gethostbyname(socket.gethostname())

    # connect to the server on local machine
    server_binding = ("128.6.13.177", port)
    cs.connect(server_binding)

    # Receive data from the server
    data_from_server=cs.recv(100)
    print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))

    # send message to server

    with open("in_proj.txt", "r") as infile, open("out_proj.txt", "w") as outfile:
        for line in infile:
            line = line.strip()
            if not line:
                continue # Skip whitespace

            cs.send(line.encode("utf-8"))

            msg_from_server = cs.recv(1024).decode("utf-8")

            outfile.write(msg_from_server + "\n")

            print(f"[C]: Sent line {line}, then received {msg_from_server}")


    # Receive modified message from server
    
    # close the client socket
    cs.close()
    exit()

if __name__ == "__main__":
    client()