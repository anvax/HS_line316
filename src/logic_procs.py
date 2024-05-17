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
            if cls.CarouselRotation and cls.rotate and not cls.drill:
                write_value_bool("ns=4;i=11", True)
                cls.counter += 1
                if cls.ColorDetection:
                    # m5 down
                    write_value_bool()
                    if cls.M5:
                        pass
                        # there are hole in object
                    else:
                        pass
                        # no hole
                    # m5 up
                    write_value_bool()
                    if cls.RedAndSilvery and cls.Silvery:
                        cls.color = "silver"
                    else:
                        if cls.RedAndSilvery:
                            cls.color = "red"
                        else:
                            cls.color = "black"
                if cls.counter == 5:
                    # drill
                    cls.drill = True
                    write_value_bool("ns=4;i=11", False)
                    write_value_bool("ns=4;i=13", False)
                    write_value_bool("ns=4;i=12", True)
                    #write_value_bool("ns=4;i=14", True)
                    write_value_bool("ns=4;i=10", True)
                    time.sleep(1)
                    write_value_bool("ns=4;i=10", False)
                    write_value_bool("ns=4;i=12", False)
                    write_value_bool("ns=4;i=13", True)
                    cls.drill = False
                    #write_value_bool("ns=4;i=11", )
                    # write_value_bool()
            elif cls.CarouselRotation:
                write_value_bool("ns=4;i=11", True)
                cls.rotate = True
                time.sleep(0.3)

            if cls.counter == 6:
                write_value_bool("ns=4;i=10", False)
                cls.finished = 1
                cls.counter = 0
                # no spin
                write_value_bool("ns=4;i=11", False)
                cls.rotate = False
        except Exception as e:
            print(e)
            # pass
