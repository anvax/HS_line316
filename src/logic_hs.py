import time

from opc_ua_operations import *
import time


class HS:
    gr_move_to_carousel = False
    gr_move_to_pack = False
    gr_move_to_conveyor = False

    # input tags
    gripper_start_sensor = ''
    gripper_pack_sensor = 'ns=4;i=24'
    gripper_conveyor_sensor = ''

    # output tags
    gripper_toggle_up_down = 'ns=4;i=33'
    gripper_open = 'ns=4;i=34'
    gripper_move_left = 'ns=4;i=32'
    gripper_move_right = 'ns=4;i=31'
    drop_puck = 'ns=4;i=35'

    def __init__(self):
        print("HS created")

    @classmethod
    def gr_down(cls, seconds):
        # gripper down
        write_value_bool(cls.gripper_toggle_up_down, True)
        time.sleep(seconds)

    @classmethod
    def gr_up(cls):
        # gripper up
        write_value_bool(cls.gripper_toggle_up_down, False)
        time.sleep(1)

    @classmethod
    def gr_move_puck_to_carousel(cls):
        # drop puck
        # "drop puck" code
        print(1)
        write_value_bool(cls.drop_puck, True)
        time.sleep(0.5)
        write_value_bool(cls.drop_puck, False)
        time.sleep(0.5)

        write_value_bool(cls.gripper_open, True)
        cls.gr_down(1)
        write_value_bool(cls.gripper_open, False)
        time.sleep(0.3)
        cls.gr_up()

        # gripper move left
        write_value_bool(cls.gripper_move_left, True)
        time.sleep(1)
        write_value_bool(cls.gripper_move_left, False)
        #
        cls.gr_down(3)
        write_value_bool(cls.gripper_open, True)
        cls.gr_up()
        write_value_bool(cls.gripper_open, False)

    @classmethod
    def gr_move_puck_to_pack(cls):
        write_value_bool(cls.gripper_open, True)
        cls.gr_down(3)
        write_value_bool(cls.gripper_open, False)
        time.sleep(0.3)
        cls.gr_up()

        gripper_middle_sensor = read_input_value(cls.gripper_pack_sensor)

        # gripper move right
        write_value_bool(cls.gripper_move_right, True)

        while not gripper_middle_sensor:
            gripper_middle_sensor = read_input_value(cls.gripper_pack_sensor)

        write_value_bool(cls.gripper_move_right, False)

        cls.gr_down(2)
        write_value_bool(cls.gripper_open, True)
        time.sleep(0.3)
        cls.gr_up()
        write_value_bool(cls.gripper_open, False)
        #
        # cls.gr_move_to_pack = True

    @classmethod
    def gr_move_puck_to_conveyor(cls):

        write_value_bool(cls.gripper_open, True)
        cls.gr_down(2)
        write_value_bool(cls.gripper_open, False)
        time.sleep(0.3)
        cls.gr_up()

        # gripper move right
        write_value_bool(cls.gripper_move_right, True)
        time.sleep(2)
        write_value_bool(cls.gripper_move_right, False)

        cls.gr_down(2)
        write_value_bool(cls.gripper_open, True)
        time.sleep(0.3)
        cls.gr_up()
        write_value_bool(cls.gripper_open, False)

        # gripper_left_sensor = read_input_value(cls.gripper_start_sensor)
        #
        # write_value_bool(cls.gripper_move_left, True)
        # while not gripper_left_sensor:
        #     gripper_left_sensor = read_input_value(cls.gripper_start_sensor)
        #
        # write_value_bool(cls.gripper_move_left, False)
        #
        # cls.gr_move_to_conveyor = True
