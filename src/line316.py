from logic_procs import *
from logic_hs import *
from logic_packs import *
from logic_ss import *


class HSline:
    client = None
    tag1 = None
    tag2 = None
    tag3 = None
    tag4 = None

    def __init__(self, client, tag1, tag2, tag3, tag4):
        self.client = client
        self.tag1 = tag1
        self.tag2 = tag2
        self.tag3 = tag3
        self.tag4 = tag4
        print("HSline created")

    @classmethod
    def update_tags(cls):
        while (1):
            cls.tag1 = read_input_value('"ns=3;s="Top_secret"."empty"', cls.client)
            cls.tag2 = read_input_value('"ns=4;s="Top_secret"."empty"', cls.client)
            cls.tag3 = read_input_value('"ns=5;s="Top_secret"."empty"', cls.client)
            cls.tag4 = read_input_value('"ns=6;s="Top_secret"."empty"', cls.client)
            # ...other tags

    @classmethod
    def start(cls):
        procs = ProcS(cls.client, cls.tag1)
        hs = HS(cls.client, cls.tag2)
        packs = PackS(cls.client, cls.tag3)
        ss = SS(cls.client, cls.tag4)

        hs.pushObject()
        hs.gripperOpen()
        hs.gripperDown()
        hs.gripperClose()
        hs.gripperUp()
        hs.gripperMoveLeft()
        hs.gripperDown()
        hs.gripperOpen()
        hs.gripperUp()
        hs.gripperClose()
        procs.spin()
        procs.pushColor()
        procs.spin()
        procs.drill()
        procs.spin()
        hs.gripperOpen()
        hs.gripperDown()
        hs.gripperClose()
        hs.gripperUp()
        hs.moveToPackS()
        hs.gripperDown()
        hs.gripperOpen()
        hs.gripperUp()
        hs.gripperClose()
        packs.pack()
        hs.gripperOpen()
        hs.gripperDown()
        hs.gripperClose()
        hs.gripperUp()
        hs.moveRight()
        hs.gripperDown()
        hs.gripperOpen()
        hs.gripperUp()
        hs.gripperClose()
        ss.sort()
