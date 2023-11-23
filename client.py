import socket
import json


def is_json(string):
    try:
        json.loads(string)
        return True
    except:
        return False


# Client
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = socket.gethostname()
PORT = 5000
connection.connect((IP, PORT))

while True:
    data_input = input('Input str in json or "break": ')
    if data_input == 'break':
        break
    data_output = is_json(data_input)
    print(data_output)

connection.close()
