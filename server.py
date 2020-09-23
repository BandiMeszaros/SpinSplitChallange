import socket
import random
import time
import argparse

HOST = "127.0.0.1"
PORT = 11111

def CLI():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("-host", dest="host", help= "Host IP", action="store")
    parser.add_argument("-port", dest="port", action="store", help="Host port number", type=int)
    args = parser.parse_args()
    return args
def serverSocket(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            i = 0
            while True:
                num = random.random()*100

                data = f"{num}"
                i += 1
                print(data)
                conn.sendall(bytes(data+"\n", "utf-8"))
                time.sleep(0.2)


def main():
    arg = CLI()

    if arg.host is None:
        host = HOST
    else:
        host = arg.host
    if arg.port is None:
        port = PORT
    else:
        port = arg.port

    serverSocket(host,port)
    return 0
if __name__ == "__main__":
    main()