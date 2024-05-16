import sys
# from line316 import *
from logic_hs import *
from logic_ss import *
from logic_procs import *
from logic_packs import *
from threading import Thread
from opc_ua_operations import client
from opc_ua_operations import *
from opcua import ua, Server, Client

tag1 = None
tag2 = None
tag3 = None
tag4 = None
tag5 = None
tag6 = None
step = 1


client

def update_tags():
    while True:
        # step = read_input_value('"fref"', client)
        tag6 = read_input_value('ns=4;i=11')
        # ...other tags


def process():
    global step
    while step == 1:
        while not procs.temp:
            procs.start()
            step = 2


if __name__ == '__main__':

    try:
        # Подключаемся к серверу
        client.connect()
        node = client.get_node('ns=4;i=11')
        print(node.server)
        print(node.nodeid)
        procs = ProcS(tag1, tag2, tag3, tag4, tag5, tag6)
        hs = HS(client, tag2)
        packs = PackS(client, tag3)
        ss = SS(client, tag4)

        t1 = Thread(target=update_tags)
        # t2 = Thread(target=process)
        t1.start()
        # t2.start()
    except Exception as e:
        print(2)
        print(e)
        # print(1)
    finally:
        # Отключаемся от сервера
        client.disconnect()
