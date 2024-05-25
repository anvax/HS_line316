import asyncio

from logic_hs import *
from logic_packs import *
from logic_procs import *
from logic_ss import *
from opc_ua_operations import *

procs = ProcS()
hs = HS()
packs = PackS()
ss = SS()
step_tag = ''
start_tag = 'ns=4;i=27'


async def start():
    write_value_bool('ns=4;i=35', True)
    while True:
        start_btn = read_input_value(start_tag)
        print(start_btn)
        if start_btn:
            write_value_bool(start_tag, False)
            gripper_put_obj_on_left()


def gripper_put_obj_on_left():
    hs.gr_move_puck_to_carousel()
    process()


def process():
    procs.start()
    gripper_move_obj_to_pack()


def gripper_move_obj_to_pack():
    hs.gr_move_puck_to_pack()
    packing()


def packing():
    packs.start()
    gripper_move_obj_to_sort()


def gripper_move_obj_to_sort():
    hs.gr_move_puck_to_conveyor()
    sorting()


def sorting():
    ss.start()
    gripper_move_to_start()


def gripper_move_to_start():
    hs.gr_move_to_start()


async def main():
    try:
        # Подключаемся к серверу
        client.connect()
        # asyncio.run(start())
        gripper_put_obj_on_left()
    finally:
        # disconnecting
        client.disconnect()


if __name__ == '__main__':
    asyncio.run(main())
