from opc_ua_operations import *


class HS:
    client = None

    def __init__(self, client, tag2):
        self.client = client
        self.tag2 = tag2
        print("HS created")

    @classmethod
    def pushObject(cls):
        write_value_bool('"ns=3;s="Top_secret"."empty"', True, cls.client)

    @classmethod
    def gripperOpen(cls):
        pass

    @classmethod
    def gripperDown(cls):
        pass

    @classmethod
    def gripperClose(cls):
        pass

    @classmethod
    def gripperUp(cls):
        pass

    @classmethod
    def gripperMoveLeft(cls):
        pass

    @classmethod
    def moveToPackS(cls):
        pass

    @classmethod
    def moveRight(cls):
        pass
