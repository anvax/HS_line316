from opc_ua_operations import *


class ProcS:
    client = None

    def __init__(self, client, tag1):
        self.client = client
        self.tag1 = tag1
        print("ProcS created")

    @classmethod
    def spin(cls):
        write_value_bool('"ns=3;s="Top_secret"."empty"', True, cls.client)

    @classmethod
    def pushColor(cls):
        pass

    @classmethod
    def drill(cls):
        pass
