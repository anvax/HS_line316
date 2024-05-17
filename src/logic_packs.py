from opc_ua_operations import *


class PackS:
    finished = 0

    def __init__(self):
        print("PackS created")

    @classmethod
    def start(cls):
        cls.finished = 1
