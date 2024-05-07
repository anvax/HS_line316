from opc_ua_operations import *


class PackS:
    client = None

    def __init__(self, client, tag3):
        self.client = client
        self.tag3 = tag3
        print("PackS created")

    @classmethod
    def pack(cls):
        write_value_bool('"ns=3;s="Top_secret"."empty"', True, cls.client)
