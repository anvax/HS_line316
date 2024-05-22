import time
from opc_ua_operations import *


class ProcS:
    # additional variables
    color = ''
    counter = 0
    finished = False
    rotate = False
    hole = False
    carousel_rotation = False

    # Input tags:
    carousel_rotation_tag = 'ns=4;i=3'
    m5_tag = ''
    red_and_silvery = ''
    silvery = ''

    # Output tags:
    drilling = "ns=4;i=10"
    carousel_rotate = "ns=4;i=11"
    drill_down = "ns=4;i=12"
    drill_up = "ns=4;i=13"
    m4_toggle = 'ns=4;i=14'
    m5_toggle = 'ns=4;i=15'

    def __init__(self):
        print("ProcS created")

    @classmethod
    def start(cls):
        cls.carousel_rotation = client.get_node(cls.carousel_rotation_tag).get_value()
        while not cls.finished:
            try:
                if cls.carousel_rotation and cls.rotate and not cls.finished:
                    cls.counter += 1
                    if cls.counter == 3:
                        # rotate to color detection
                        time.sleep(0.1)
                        write_value_bool(cls.carousel_rotate, False)
                        time.sleep(1)
                        cls.red_and_silvery = read_input_value(cls.red_and_silvery)
                        cls.silvery = read_input_value(cls.silvery)

                        if cls.red_and_silvery and cls.silvery:
                            cls.color = "silver"
                        elif cls.red_and_silvery:
                            cls.color = "red"
                        else:
                            cls.color = "black"

                        # m5 down
                        write_value_bool(cls.m5_up_down, True)
                        time.sleep(0.5)
                        cls.M5 = read_input_value(cls.m5_tag)

                        if cls.M5:
                            cls.hole = True
                        else:
                            cls.hole = False

                        # m5 up
                        write_value_bool(cls.m5_up_down,  False)
                        time.sleep(0.5)
                        write_value_bool("ns=4;i=11", True)

                    elif cls.counter == 4:
                        # Rotate to drill place
                        time.sleep(0.2)
                        write_value_bool("ns=4;i=11", False)
                        time.sleep(1)

                        # drill the puck
                        if not cls.hole:
                            # drill
                            write_value_bool(cls.drill_down, True)
                            time.sleep(0.6)
                            write_value_bool(cls.drill_down, False)
                            write_value_bool(cls.drilling, True)
                            time.sleep(1)
                            write_value_bool(cls.drilling, False)

                            write_value_bool(cls.drill_up, True)
                            time.sleep(0.6)
                            write_value_bool(cls.drill_up, False)

                        # rotate carousel to start place
                        write_value_bool(cls.carousel_rotate, True)
                        time.sleep(0.2)
                        write_value_bool(cls.carousel_rotate, False)
                        cls.counter = 0
                        cls.rotate = False
                        cls.finished = True

                elif cls.carousel_rotation and not cls.finished:
                    write_value_bool(cls.carousel_rotate, True)
                    cls.rotate = True
                    time.sleep(0.3)

            except Exception as e:
                print(e)
