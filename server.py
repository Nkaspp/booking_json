import socket

#server
def server_program():
    host = socket.gethostname()
    port = 5000
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address), str(conn))
server_program()

