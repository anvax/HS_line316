from opc_ua_operations import *


class SS:
    finished = 0

    def __init__(self):
        print("SS created")

    @classmethod
    def start(cls):
        cls.finished = 1
