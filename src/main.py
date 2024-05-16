import sys
#from line316 import *
from logic_hs import *
from logic_ss import *
from logic_procs import *
from logic_packs import *
from threading import Thread
from opc_ua_operations import *
from opcua import ua, Server, Client
tag1 = None
tag2 = None
tag3 = None
tag4 = None
tag5 = None
step = None
client = Client("opc.tcp://192.168.3.11:5005")


def update_tags():
    while True:
        step = read_input_value('"fref"', client)
        tag1 = read_input_value('"ns=3;s="Top_secret"."empty"', client)
        tag2 = read_input_value('"ns=4;s="Top_secret"."empty"', client)
        tag3 = read_input_value('"ns=5;s="Top_secret"."empty"', client)
        tag4 = read_input_value('"ns=6;s="Top_secret"."empty"', client)
        tag5 = read_input_value('"ns=7;s="Top_secret"', client)
        # ...other tags
def procs():
    while step==1:
        while not procs.temp:
            procs.start()


if __name__ == '__main__':

    try:
        # Подключаемся к серверу
        client.connect()
        procs = ProcS(client, tag1, tag2, tag3, tag4, tag5)
        hs = HS(client, tag2)
        packs = PackS(client, tag3)
        ss = SS(client, tag4)
        HSline316 = HSline(client, tag1, tag2, tag3, tag4)
        t1 = Thread(target=HSline316.update_tags())
        t1.start()
        t2 = Thread(target=HSline316.start())
        t2.start()
    finally:
        # Отключаемся от сервера
        client.disconnect()
