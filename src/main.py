import asyncio
from threading import Thread

from logic_hs import *
from logic_packs import *
from logic_procs import *
from logic_ss import *
from opc_ua_operations import *

step = client.get_node(ProcS.carousel_rotation_tag).get_value()

procs = ProcS()
hs = HS()
packs = PackS()
ss = SS()


def gripper_put_obj_on_left():
    global step
    if not hs.gr_move_to_carousel and step == 0:
        hs.gr_move_puck_to_carousel()
    else:
        # write_value_int(ProcS.carousel_rotation_tag, 1)
        step = 1
        process()


def process():
    global step
    if not procs.finished and step == 1:
        procs.start()
    else:
        # write_value_int("ns=4;i=3", 2)
        step = 2
        gripper_move_obj_to_pack()


def gripper_move_obj_to_pack():
    global step
    if not hs.gr_move_to_pack and step == 2:
        hs.gr_move_puck_to_pack()
    else:
        # write_value_int("ns=4;i=3", 3)
        step = 3
        packing()


def packing():
    global step
    if not packs.finished and step == 3:
        packs.start()
    else:
        # write_value_int("ns=4;i=3", 4)
        step = 4
        gripper_move_obj_to_sort()


def gripper_move_obj_to_sort():
    global step
    if not hs.gr_move_to_conveyor and step == 4:
        hs.gr_move_puck_to_conveyor()
    else:
        # write_value_int("ns=4;i=3", 5)
        step = 5
        sorting()


def sorting():
    global step
    if not ss.finished and step == 5:
        ss.start()
    else:
        # write_value_int("ns=4;i=3", 0)
        step = 0


def main():
    try:
        # Подключаемся к серверу
        client.connect()
        gripper_put_obj_on_left()

    finally:
        # disconnecting
        client.disconnect()


if __name__ == '__main__':
    main()
