import time
from opc_ua_operations import *


class ProcS:
    # additional variables
    counter = -1
    finished = False
    rotate = False
    hole = False
    carousel_rotation = False
    M5 = False

    red_tag = 'ns=4;i=24'
    silver_tag = 'ns=4;i=26'
    black_tag = 'ns=4;i=25'

    # Input tags:
    carousel_rotation_tag = 'ns=4;i=3'
    m5_tag = 'ns=4;i=4'
    red_and_silvery = 'ns=4;i=6'
    silvery = 'ns=4;i=7'

    # Output tags:
    drilling = "ns=4;i=12"
    carousel_rotate = "ns=4;i=13"
    drill_down = "ns=4;i=14"
    drill_up = "ns=4;i=15"
    m4_toggle = 'ns=4;i=16'
    m5_toggle = 'ns=4;i=17'

    def __init__(self):
        print("ProcS created")

    @classmethod
    def start(cls):
        cls.carousel_rotation = client.get_node(cls.carousel_rotation_tag).get_value()
        write_value_bool(cls.carousel_rotate, True)
        while not cls.finished:
            try:
                print(cls.counter)
                if cls.counter < 4:
                    cls.counter += 1
                if not cls.finished and cls.counter >= 3:
                    if cls.counter == 4:
                        # rotate to color detection
                        time.sleep(0.1)
                        write_value_bool(cls.carousel_rotate, False)
                        time.sleep(1)
                        cls.red_and_silvery = read_input_value(cls.red_and_silvery)
                        cls.silvery = read_input_value(cls.silvery)

                        if cls.red_and_silvery and cls.silvery:
                            print('Silvery')
                            write_value_bool(cls.silver_tag, True)
                        elif cls.red_and_silvery:
                            print('Red')
                            write_value_bool(cls.red_tag, True)
                        else:
                            print('Black')
                            write_value_bool(cls.black_tag, True)

                        # m5 down
                        write_value_bool(cls.m5_toggle, True)
                        time.sleep(0.5)
                        cls.M5 = read_input_value(cls.m5_tag)

                        if cls.M5:
                            cls.hole = True
                        else:
                            cls.hole = False

                        # m5 up
                        write_value_bool(cls.m5_toggle, False)
                        time.sleep(0.5)
                        cls.counter += 1
                        time.sleep(1)
                        write_value_bool(cls.carousel_rotate, True)


                    elif cls.counter == 5:
                        # Rotate to drill place
                        write_value_bool(cls.carousel_rotate, False)
                        time.sleep(1)

                        # drill the puck
                        if cls.hole:
                            # drill
                            write_value_bool(cls.m4_toggle, True)
                            time.sleep(0.1)
                            write_value_bool(cls.drill_down, True)
                            time.sleep(0.6)
                            write_value_bool(cls.drill_down, False)
                            write_value_bool(cls.drilling, True)
                            time.sleep(1)
                            write_value_bool(cls.drilling, False)

                            write_value_bool(cls.drill_up, True)
                            time.sleep(0.6)
                            write_value_bool(cls.drill_up, False)
                            write_value_bool(cls.m4_toggle, False)

                        # rotate carousel to start place
                        write_value_bool(cls.carousel_rotate, True)
                        time.sleep(0.2)
                        write_value_bool(cls.carousel_rotate, False)
                        cls.counter = -1
                        cls.rotate = False
                        cls.finished = True
                time.sleep(0.8)
            except Exception as e:
                print(e)
