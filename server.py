import socket
import random
import datetime
from lib import colors

class settings:
    HOST = "127.0.0.1"
    PORT = random.randint(1, 9999)
    TIME = datetime.datetime.now()

def time():
    return ("%s%d:%d:%d%s | %s" % (colors.get("green", 1), settings.TIME.hour, settings.TIME.minute, settings.TIME.second, colors.get("reset", 0), colors.get("purple", 1)))

def server():
    s = socket.socket()

    s.bind((settings.HOST, settings.PORT))
    s.listen(5)
    print("%s [%s:%d] Server started" % (time(), settings.HOST, settings.PORT))

    while True:
        c, addr = s.accept()
        print("%s [%s:%d] %s connected" % (time(), settings.HOST, settings.PORT, addr))
        target = input("%s [%s:%d] Filename: " % (time(), settings.HOST, settings.PORT))
        f = open(target, "wb")

        listen = c.recv(1024)

        print("%s [%s:%d] Starting transfert..." % (time(), settings.HOST, settings.PORT))
        while (listen):
            f.write(listen)
            listen = c.recv(1024)
        f.close()

        print("%s [%s:%d] Transfert finished" % (time(), settings.HOST, settings.PORT))
        c.close()

def main():
    print("%s [%s:%d] Starting server..." % (time(), settings.HOST, settings.PORT))

    server()

main()
