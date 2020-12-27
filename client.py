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

def client():
    s = socket.socket()
    s.connect((settings.HOST, settings.PORT))
    print("%s [%s:%d] Connected" % (time(), settings.HOST, settings.PORT))

    target = input("%s [%s:%d] File to send: " % (time(), settings.HOST, settings.PORT))

    f = open(target, "rb")
    print("%s [%s:%d] Sending '%s'..." % (time(), settings.HOST, settings.PORT, target))

    data = f.read(1024)
    while (data):
        s.send(data)
        data = f.read(1024)

    f.close()
    print("%s [%s:%d] Transfert finished" % (time(), settings.HOST, settings.PORT))
    s.shutdown(socket.SHUT_WR)
    s.close()

def main():
    server_id = input("Server configuration (host:port): ")
    settings.HOST = server_id.split(':')[0]
    settings.PORT = int(server_id.split(':')[1])
    
    client()

main()