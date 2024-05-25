import time

from opc_ua_operations import *
import time


class HS:
    gr_move_to_carousel = False
    gr_move_to_pack = False
    gr_move_to_conveyor = False

    # input tags
    gripper_start_sensor = 'ns=4;i=31'
    gripper_pack_sensor = 'ns=4;i=30'
    gripper_conveyor_sensor = 'ns=4;i=32'

    # output tags
    gripper_toggle_up_down = 'ns=4;i=39'
    gripper_open = 'ns=4;i=40'
    gripper_move_left = 'ns=4;i=38'
    gripper_move_right = 'ns=4;i=37'
    drop_puck = 'ns=4;i=41'
    green_tag = 'ns=4;i=34'
    yellow_tag = 'ns=4;i=35'

    # output packing tags
    push_box = 'ns=4;i=43'
    fix_box_upper_side = 'ns=4;i=44'

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
        time.sleep(1.5)

    @classmethod
    def gr_move_puck_to_carousel(cls):

        write_value_bool(cls.yellow_tag, False)
        write_value_bool(cls.green_tag, True)
        write_value_bool(cls.drop_puck, True)
        time.sleep(0.7)
        write_value_bool(cls.drop_puck, False)
        time.sleep(0.5)

        write_value_bool(cls.gripper_open, True)
        cls.gr_down(1.5)
        write_value_bool(cls.gripper_open, False)
        time.sleep(0.3)
        cls.gr_up()

        # gripper move left
        write_value_bool(cls.gripper_move_left, True)
        time.sleep(1)
        write_value_bool(cls.gripper_move_left, False)
        #
        cls.gr_down(2)
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
        t1 = 0
        t2 = 0
        while not gripper_middle_sensor:
            t1 = time.time()
            t2 = time.time()
            gripper_middle_sensor = read_input_value(cls.gripper_pack_sensor)
            print(time.time() - t2)

        write_value_bool(cls.gripper_move_right, False)
        print(time.time()-t1)
        write_value_bool(cls.push_box, True)
        time.sleep(1)
        write_value_bool(cls.push_box, False)
        write_value_bool(cls.fix_box_upper_side, True)
        time.sleep(1)

        cls.gr_down(0.6)
        write_value_bool(cls.gripper_open, True)
        time.sleep(0.3)
        cls.gr_up()
        time.sleep(1)
        write_value_bool(cls.gripper_open, False)
        #
        # cls.gr_move_to_pack = True

    @classmethod
    def gr_move_puck_to_conveyor(cls):

        write_value_bool(cls.gripper_open, True)
        cls.gr_down(2.5)
        write_value_bool(cls.gripper_open, False)
        time.sleep(0.6)
        cls.gr_up()
        time.sleep(1)
        # gripper move right
        write_value_bool(cls.gripper_move_right, True)
        time.sleep(2)
        write_value_bool(cls.gripper_move_right, False)

        cls.gr_down(2)
        write_value_bool(cls.gripper_open, True)
        time.sleep(0.3)
        cls.gr_up()
        write_value_bool(cls.gripper_open, False)

    @classmethod
    def gr_move_to_start(cls):

        gripper_start_sensor = read_input_value(cls.gripper_start_sensor)

        # gripper move left
        write_value_bool(cls.gripper_move_left, True)
        t1 = 0
        while not gripper_start_sensor:
            t1 = time.time()
            gripper_start_sensor = read_input_value(cls.gripper_start_sensor)

        write_value_bool(cls.gripper_move_left, False)
        print(time.time()-t1)
        write_value_bool(cls.green_tag, False)
        write_value_bool(cls.yellow_tag, True)
