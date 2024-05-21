import time

from opc_ua_operations import *


class HS:
    gr_move_to_carousel = False
    gr_move_to_pack = False
    gr_move_to_conveyor = False

    # input tags
    graider_start_sensor = ''
    graider_pack_sensor = ''
    graider_conveyor_sensor = ''

    # output tags
    graider_down = ''
    graider_up = ''
    graider_move_left = ''
    graider_move_right = ''

    def __init__(self):
        print("HS created")

    @classmethod
    def gr_down(cls):
        # graider down
        write_value_bool(cls.graider_down, True)
        time.sleep(1)
        write_value_bool(cls.graider_down, False)

    @classmethod
    def gr_up(cls):
        # graider up
        write_value_bool(cls.graider_up, True)
        time.sleep(1)
        write_value_bool(cls.graider_up, False)

    @classmethod
    def gr_move_puck_to_carousel(cls):
        # drop puck
        # "drop puck" code

        cls.gr_down()
        cls.gr_up()

        # graider move left
        write_value_bool(cls.graider_move_left, True)
        time.sleep(3)
        write_value_bool(cls.graider_move_left, False)

        cls.gr_down()
        cls.gr_up()

        cls.gr_move_to_carousel = True

    @classmethod
    def gr_move_puck_to_pack(cls):
        cls.gr_down()
        cls.gr_up()

        graider_middle_sensor = read_input_value(cls.graider_pack_sensor)

        # graider move right
        write_value_bool(cls.graider_move_right, True)

        while not graider_middle_sensor:
            graider_middle_sensor = read_input_value(cls.graider_pack_sensor)

        write_value_bool(cls.graider_move_right, False)

        cls.gr_down()
        cls.gr_up()

        cls.gr_move_to_pack = True

    @classmethod
    def gr_move_puck_to_conveyor(cls):

        cls.gr_down()
        cls.gr_up()

        # graider move right
        write_value_bool(cls.graider_move_right, True)
        time.sleep(3)
        write_value_bool(cls.graider_move_right, False)

        cls.gr_down()
        cls.gr_up()

        graider_left_sensor = read_input_value(cls.graider_start_sensor)

        write_value_bool(cls.graider_move_left, True)
        while not graider_left_sensor:
            graider_left_sensor = read_input_value(cls.graider_start_sensor)

        write_value_bool(cls.graider_move_left, False)

        cls.gr_move_to_conveyor = True
