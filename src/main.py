import sys
from line316 import *
from threading import Thread
from opc_ua_operations import *
from opcua import ua, Server, Client

if __name__ == '__main__':

    client = Client("opc.tcp://192.168.3.11:5005")
    tag1 = None
    tag2 = None
    tag3 = None
    tag4 = None
    try:
        # Подключаемся к серверу
        client.connect()
        HSline316 = HSline(client, tag1, tag2, tag3, tag4)
        t1 = Thread(target=HSline316.update_tags())
        t1.start()
        t2 = Thread(target=HSline316.start())
        t2.start()
    finally:
        # Отключаемся от сервера
        client.disconnect()
