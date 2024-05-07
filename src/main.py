import sys
from line316 import *
from opc_ua_operations import *
from opcua import ua, Server, Client


if __name__ == '__main__':

    client = Client("opc.tcp://192.168.3.11:5005")

    try:
        # Подключаемся к серверу
        client.connect()
        root = client.get_root_node()
        print("root node : " + str(root))

        tag1 = read_input_value('"ns=3;s="Top_secret"."empty"', client)
        tag2 = read_input_value('"ns=4;s="Top_secret"."empty"', client)
        tag3 = read_input_value('"ns=5;s="Top_secret"."empty"', client)
        tag4 = read_input_value('"ns=6;s="Top_secret"."empty"', client)
        #...other tags
        HSline316 = HSline(client, tag1, tag2, tag3, tag4)
        HSline316.start()
    finally:
        # Отключаемся от сервера
        client.disconnect()







