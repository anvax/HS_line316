# from line316 import *
import asyncio
from threading import Thread

from logic_hs import *
from logic_packs import *
from logic_procs import *
from logic_ss import *
from opc_ua_operations import *

tag1 = None
tag2 = None
tag3 = None
tag4 = None
tag5 = None
tag6 = None
step = 1

procs = ProcS(tag1, tag2, tag3, tag4, tag5, tag6)
hs = HS(client, tag2)
packs = PackS(client, tag3)
ss = SS(client, tag4)


async def process():
    global step
    while step == 1:
        while not procs.temp:
            procs.start()
            step = 2


def main():
    try:
        # Подключаемся к серверу
        client.connect()
        # node = client.get_node('ns=4;i=11')
        # print(node.get_value())
        asyncio.run(process())
        # t2 = Thread(target=process)
        # t1.start()
        # t2.start()
    finally:
        # Отключаемся от сервера
        client.disconnect()

if __name__ == '__main__':
    main()