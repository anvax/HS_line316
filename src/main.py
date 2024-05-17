# from line316 import *
import asyncio
from threading import Thread

from logic_hs import *
from logic_packs import *
from logic_procs import *
from logic_ss import *
from opc_ua_operations import *

step = client.get_node('ns=4;i=3').get_value()

procs = ProcS()
hs = HS()
packs = PackS()
ss = SS()


async def gripper_put_obj_on_left():
    global step
    while step == 0:
        step = client.get_node('ns=4;i=3').get_value()
        while not hs.grLeftFinished:
            hs.gr_left_start()
            write_value_int("ns=4;i=3", 1)
            step = client.get_node('ns=4;i=3').get_value()


async def process():
    global step
    while step == 1:
        step = client.get_node('ns=4;i=3').get_value()
        while not procs.finished:
            procs.start()
            write_value_int("ns=4;i=3", 2)
            step = client.get_node('ns=4;i=3').get_value()


async def gripper_move_obj_to_pack():
    global step
    while step == 2:
        step = client.get_node('ns=4;i=3').get_value()
        while not hs.grMidFinished:
            hs.gr_mid_start()
            write_value_int("ns=4;i=3", 3)
            step = client.get_node('ns=4;i=3').get_value()


async def packing():
    global step
    while step == 3:
        step = client.get_node('ns=4;i=3').get_value()
        while not procs.finished:
            packs.start()
            write_value_int("ns=4;i=3", 4)
            step = client.get_node('ns=4;i=3').get_value()


async def gripper_move_obj_to_sort():
    global step
    while step == 4:
        step = client.get_node('ns=4;i=3').get_value()
        while not procs.finished:
            hs.gr_right_start()
            write_value_int("ns=4;i=3", 5)
            step = client.get_node('ns=4;i=3').get_value()


async def sorting():
    global step
    while step == 5:
        step = client.get_node('ns=4;i=3').get_value()
        while not procs.finished:
            ss.start()
            write_value_int("ns=4;i=3", 0)
            step = client.get_node('ns=4;i=3').get_value()


def main():
    try:
        # Подключаемся к серверу
        client.connect()
        # node = client.get_node('ns=4;i=11')
        # print(node.get_value())

        asyncio.run(gripper_put_obj_on_left())
        asyncio.run(process())
        asyncio.run(gripper_move_obj_to_pack())
        asyncio.run(packing())
        asyncio.run(gripper_move_obj_to_sort())
        asyncio.run(sorting())

        # t2 = Thread(target=process)
        # t1.start()
        # t2.start()
    finally:
        # disconnecting
        client.disconnect()


if __name__ == '__main__':
    main()
