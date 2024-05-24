import time

from opc_ua_operations import *


class SS:
    finished = 0
    box_is_down = False
    box_on_conveyor = False
    red = False
    silver = False
    black = False
    # input
    box_is_down_tag = 'ns=4;i=9'
    box_on_conveyor_tag = 'ns=4;i=10'
    red_tag = 'ns=4;i=24'
    silver_tag = 'ns=4;i=26'
    black_tag = 'ns=4;i=25'
    # output
    move_conveyor_right = 'ns=4;i=19'
    move_conveyor_left = 'ns=4;i=20'
    push_silver = 'ns=4;i=21'
    push_red = 'ns=4;i=22'

    def __init__(self):
        print("SS created")

    @classmethod
    def start(cls):
        cls.box_on_conveyor = read_input_value(cls.box_on_conveyor_tag)
        cls.box_is_down = read_input_value(cls.box_is_down_tag)
        cls.red = read_input_value(cls.red_tag)
        cls.silver = read_input_value(cls.silver_tag)
        cls.black = read_input_value(cls.black_tag)
        cls.red = True
        if cls.box_on_conveyor:
            if cls.red:
                write_value_bool(cls.push_red, True)
                write_value_bool(cls.push_silver, False)
            elif cls.silver:
                write_value_bool(cls.push_red, False)
                write_value_bool(cls.push_silver, True)
            write_value_bool(cls.move_conveyor_right, True)
            while not cls.box_is_down:
                cls.box_is_down = read_input_value(cls.box_is_down_tag)

        if cls.box_is_down:
            write_value_bool(cls.move_conveyor_right, False)
            write_value_bool(cls.push_red, False)
            write_value_bool(cls.push_silver, False)
            write_value_bool(cls.red_tag, False)
            write_value_bool(cls.silver_tag, False)
            write_value_bool(cls.black_tag, False)

        cls.finished = 1
