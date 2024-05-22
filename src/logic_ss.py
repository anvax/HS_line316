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
    box_is_down_tag = ''
    box_on_conveyor_tag = ''
    red_tag = ''
    silver_tag = ''
    black_tag = ''
    # output
    move_conveyor_right = ''
    move_conveyor_left = ''
    push_silver = ''
    push_red = ''

    def __init__(self):
        print("SS created")

    @classmethod
    def start(cls):
        cls.box_on_conveyor = client.get_node(cls.box_on_conveyor_tag).get_value()
        cls.box_is_down = client.get_node(cls.box_is_down).get_value()
        cls.red = client.get_node(cls.red).get_value()
        cls.silver = client.get_node(cls.silver).get_value()
        cls.black = client.get_node(cls.black).get_value()
        if cls.box_on_conveyor:
            if cls.red:
                write_value_bool(cls.push_red, True)
                write_value_bool(cls.push_silver, False)
            elif cls.silver:
                write_value_bool(cls.push_red, False)
                write_value_bool(cls.push_silver, True)
            write_value_bool(cls.move_conveyor_right, True)
        if cls.box_is_down:
            write_value_bool(cls.move_conveyor_right, False)
            write_value_bool(cls.push_red, False)
            write_value_bool(cls.push_silver, False)
        cls.finished = 1
