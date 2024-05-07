import sys
from line316 import *
from opcua import ua, Server, Client



def main():
    HSline316 = HSline
    client = Client("opc.tcp://localhost:4840/freeopcua/server/")

    try:
        # Подключаемся к серверу
        client.connect()

        # Получаем объект Node для тэга, который хотим изменить
        node = client.get_node("ns=2;i=2")  # Пример адреса тэга
        # Считываем значение тэга
        value = node.get_value()

        #HSline316.start(куча тегов)


        # Записываем новое значение тэга
        node.set_value(False)

        # Считываем и выводим новое значение тэга
        new_value = node.get_value()
        print(f"Новое значение тэга: {new_value}")

        # Другие операции с тэгами...

    finally:
        # Отключаемся от сервера
        client.disconnect()





if __name__ == '__main__':
    main()
