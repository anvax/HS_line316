# from line316 import *
import asyncio
from threading import Thread

from logic_hs import *
from logic_packs import *
from logic_procs import *
from logic_ss import *
from opc_ua_operations import *

step: int = client.get_node('ns=4;i=3').get_value()

procs = ProcS()
hs = HS()
packs = PackS()
ss = SS()


async def gripper_put_obj_on_left():
    global step
    while step == 0:
        step = client.get_node('ns=4;i=3').get_value()
        if not hs.grLeftFinished:
            hs.gr_left_start()
        else:
            write_value_int("ns=4;i=3", 1)
            step = 1


async def process():
    global step
    while step == 1:
        step = client.get_node('ns=4;i=3').get_value()
        if not procs.finished:
            procs.start()
        else:
            write_value_int("ns=4;i=3", 2)
            step = 2


async def gripper_move_obj_to_pack():
    global step
    while step == 2:
        step = client.get_node('ns=4;i=3').get_value()
        if not hs.grMidFinished:
            hs.gr_mid_start()
        else:
            write_value_int("ns=4;i=3", 3)
            step = 3


async def packing():
    global step
    while step == 3:
        step = client.get_node('ns=4;i=3').get_value()
        if not packs.finished:
            packs.start()
        else:
            write_value_int("ns=4;i=3", 4)
            step = 4


async def gripper_move_obj_to_sort():
    global step
    while step == 4:
        step = client.get_node('ns=4;i=3').get_value()
        if not hs.grRightFinished:
            hs.gr_right_start()
        else:
            write_value_int("ns=4;i=3", 5)
            step = 5


async def sorting():
    global step
    while step == 5:
        step = client.get_node('ns=4;i=3').get_value()
        if not ss.finished:
            ss.start()
        else:
            write_value_int("ns=4;i=3", 0)
            step = 0


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
