import time
from opc_ua_operations import *


class ProcS:
    color = None
    counter = 0
    finished = 0
    # Input tags:
    CarouselRotation = None
    M5 = None
    ColorDetection = None
    RedAndSilvery = None
    Silvery = None
    rotate = False
    drill = False
    hole = False

    # Output tags:
    Spin = None

    def __init__(self):
        print("ProcS created")

    @classmethod
    def start(cls):
        serv_node = client.get_node('ns=4;i=11')
        # print('Carousel Rotation: ', serv_node.get_value())
        cls.CarouselRotation = client.get_node('ns=4;i=3').get_value()
        #cls.ColorDetection=client.get_node('ns=4,i=11').get_value()
        # print(cls.CarouselRotation)

        try:
            # print(cls.counter)
            #print(cls.rotate)
            if cls.CarouselRotation and cls.rotate and not cls.finished:
                cls.counter += 1
                if cls.counter == 3:
                    # m5 down
                    time.sleep(0.1)
                    write_value_bool("ns=4;i=11", False)
                    time.sleep(0.4)
                    cls.RedAndSilvery = read_input_value('')
                    cls.Silvery = read_input_value('')

                    if cls.RedAndSilvery and cls.Silvery:
                        cls.color = "silver"
                    else:
                        if cls.RedAndSilvery:
                            cls.color = "red"
                        else:
                            cls.color = "black"

                    #M5 down
                    write_value_bool("", True)
                    time.sleep(0.5)
                    cls.M5 = read_input_value('')

                    if cls.M5:
                        cls.hole = True
                    else:
                        cls.hole = False
                    # m5 up
                    write_value_bool("Опустить M5",  False)
                    write_value_bool('Поднять M5', True)
                    time.sleep(0.5)
                    write_value_bool("ns=4;i=11", True)

                elif cls.counter == 4:
                    # Провернуть до положения дрели
                    time.sleep(0.2)
                    write_value_bool("ns=4;i=11", False)
                    time.sleep(1)
                    if not cls.hole:
                        # drill
                        write_value_bool("ns=4;i=12", True) # Opuskanie dreli
                        time.sleep(0.6)
                        write_value_bool("ns=4;i=12", False)  # Opuskanie dreli
                        write_value_bool("ns=4;i=10", True) # Sverlenie
                        time.sleep(1)
                        write_value_bool("ns=4;i=10", False) # Sverlenie

                        write_value_bool("ns=4;i=13", True)
                        time.sleep(0.6)

                    write_value_bool("ns=4;i=11", True)
                    time.sleep(0.2)
                    write_value_bool("ns=4;i=11", False)
                    cls.counter = 0
                    cls.finished = True
                    cls.rotate = False

            elif cls.CarouselRotation and not cls.finished:
                write_value_bool("ns=4;i=11", True)
                cls.rotate = True
                time.sleep(0.3)

        except Exception as e:
            print(e)
            # pass
