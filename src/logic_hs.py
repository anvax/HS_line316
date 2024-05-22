import time

from opc_ua_operations import *
import time


class HS:
    gr_move_to_carousel = False
    gr_move_to_pack = False
    gr_move_to_conveyor = False

    # input tags
    gripper_start_sensor = ''
    gripper_pack_sensor = ''
    gripper_conveyor_sensor = ''

    # output tags
    gripper_down = ''
    gripper_up = ''
    gripper_move_left = ''
    gripper_move_right = ''

    def __init__(self):
        print("HS created")

    @classmethod
    def gr_down(cls):
        # gripper down
        write_value_bool(cls.gripper_down, True)
        time.sleep(1)
        write_value_bool(cls.gripper_down, False)

    @classmethod
    def gr_up(cls):
        # gripper up
        write_value_bool(cls.gripper_up, True)
        time.sleep(1)
        write_value_bool(cls.gripper_up, False)

    @classmethod
    def gr_move_puck_to_carousel(cls):
        # drop puck
        # "drop puck" code

        cls.gr_down()
        cls.gr_up()

        # gripper move left
        write_value_bool(cls.gripper_move_left, True)
        time.sleep(3)
        write_value_bool(cls.gripper_move_left, False)

        cls.gr_down()
        cls.gr_up()

        cls.gr_move_to_carousel = True

    @classmethod
    def gr_move_puck_to_pack(cls):
        cls.gr_down()
        cls.gr_up()

        gripper_middle_sensor = read_input_value(cls.gripper_pack_sensor)

        # gripper move right
        write_value_bool(cls.gripper_move_right, True)

        while not gripper_middle_sensor:
            gripper_middle_sensor = read_input_value(cls.gripper_pack_sensor)

        write_value_bool(cls.gripper_move_right, False)

        cls.gr_down()
        cls.gr_up()

        cls.gr_move_to_pack = True

    @classmethod
    def gr_move_puck_to_conveyor(cls):

        cls.gr_down()
        cls.gr_up()

        # gripper move right
        write_value_bool(cls.gripper_move_right, True)
        time.sleep(3)
        write_value_bool(cls.gripper_move_right, False)

        cls.gr_down()
        cls.gr_up()

        gripper_left_sensor = read_input_value(cls.gripper_start_sensor)

        write_value_bool(cls.gripper_move_left, True)
        while not gripper_left_sensor:
            gripper_left_sensor = read_input_value(cls.gripper_start_sensor)

        write_value_bool(cls.gripper_move_left, False)

        cls.gr_move_to_conveyor = True
