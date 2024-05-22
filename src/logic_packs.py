import time

from opc_ua_operations import *


class PackS:
    finished = 0
    bend = ''
    retainer = ''
    flap_down = ''
    flap_up = ''

    def __init__(self):
        print("PackS created")

    @classmethod
    def start(cls):
        write_value_bool(cls.retainer, True)
        time.sleep(1)
        write_value_bool(cls.bend, True)
        time.sleep(1)
        write_value_bool(cls.retainer, False)
        time.sleep(1)
        write_value_bool(cls.flap_down, True)
        time.sleep(1)
        write_value_bool(cls.flap_down, False)
        time.sleep(1)
        write_value_bool(cls.flap_up, True)
        time.sleep(1)
        write_value_bool(cls.bend, False)
        time.sleep(1)


        cls.finished = 1
