from logic_procs import *
from logic_hs import *
from logic_packs import *
from logic_ss import *


class HSline:
    def __init__(self):
        print("HSline created")

    @classmethod
    def start(cls):
        procs = ProcS
        hs = HS
        packs = PackS
        ss = SS

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
