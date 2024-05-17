from opc_ua_operations import *


class HS:
    grLeftFinished = 0
    grMidFinished = 0
    grRightFinished = 0

    def __init__(self):
        print("HS created")

    @classmethod
    def gr_left_start(cls):
        cls.grLeftFinished = 1

    @classmethod
    def gr_mid_start(cls):
        cls.grMidFinished = 1

    @classmethod
    def gr_right_start(cls):
        cls.grRightFinished = 1
