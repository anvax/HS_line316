from opc_ua_operations import *


class SS:
    client = None

    def __init__(self, client, tag4):
        self.client = client
        self.tag4 = tag4
        print("SS created")

    @classmethod
    def sort(cls):
        write_value_bool('"ns=3;s="Top_secret"."empty"', True, cls.client)
