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
start_tag = 'ns=4;i=45'


async def start():
    # step = read_input_value(step_tag)
    # step_program = {
    #     0: gripper_put_obj_on_left,
    #     1: process,
    #     2: gripper_move_obj_to_pack,
    #     3: packing,
    #     4: gripper_move_obj_to_sort,
    #     5: sorting,
    # }
    while True:
        start_btn = read_input_value(start_tag)
        print(start_btn)
        if start_btn:
            write_value_bool(start_tag, False)
            # step_program[step]()
            gripper_put_obj_on_left()


def gripper_put_obj_on_left():
    hs.gr_move_puck_to_carousel()
    # step = read_input_value(step_tag)
    # write_value_int(step_tag, step+1)
    process()


def process():
    procs.start()
    # step = read_input_value(step_tag)
    # write_value_int(step_tag, step+1)
    # gripper_move_obj_to_pack()


def gripper_move_obj_to_pack():
    hs.gr_move_puck_to_pack()
    # step = read_input_value(step_tag)
    # write_value_int(step_tag, step+1)
    # packing()


def packing():
    if not packs.finished:
        packs.start()
        step = read_input_value(step_tag)
        write_value_int(step_tag, step+1)
        gripper_move_obj_to_sort()


def gripper_move_obj_to_sort():
    hs.gr_move_puck_to_conveyor()
    # step = read_input_value(step_tag)
    # write_value_int(step_tag, step+1)
    sorting()


def sorting():
    ss.start()
    # step = read_input_value(step_tag)
    # write_value_int(step_tag, 0)
    # step = 0


async def main():
    try:
        # Подключаемся к серверу
        client.connect()
        # gripper_put_obj_on_left()
        # await asyncio.create_task(start())
        # process()
        # sorting()
        # gripper_move_obj_to_pack()
        gripper_move_obj_to_sort()
    finally:
        # disconnecting
        client.disconnect()


if __name__ == '__main__':
    asyncio.run(main())
