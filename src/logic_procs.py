from opc_ua_operations import *


class ProcS:
    client = None
    color = None
    counter = 0
    temp=0
    #Input tags:
    CarouselRotation = None
    M5 = None
    ColorDetection = None
    RedAndSilvery = None
    Silvery = None

    #Output tags:
    #...

    def __init__(self, client, tag1, tag2,tag3,tag4,tag5):
        self.client = client
        self.CarouselRotation = tag1
        self.M5 = tag2
        self.ColorDetection=tag3
        self.RedAndSilvery=tag4
        self.Silvery=tag5
        print("ProcS created")

    @classmethod
    def start(cls):
        #spin
        write_value_bool()
        if cls.CarouselRotation:
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
                write_value_bool()
        if cls.counter == 6:
            cls.temp=1
            cls.counter = 0
            # no spin
            write_value_bool()

