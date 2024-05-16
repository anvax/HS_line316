from opcua import ua, Server, Client
client = Client("opc.tcp://10.160.160.61:4840")

def read_input_value(node_id):
    try:

        client_node = client.get_node(node_id)
        client_node_value = client_node.get_value()
        # print("value of : " + str(client_node) + ' : ' + str(client_node_value))
    except Exception as e:
        return None

    return client_node_value


def write_value_int(node_id, value):
    client_node = client.get_node(node_id)
    client_node_value = value
    client_node_dv = ua.DataValue(ua.Variant(client_node_value, ua.VariantType.Int16))
    client_node.set_value(client_node_dv)
    # print("value of : " + str(client_node) + ' : ' + str(client_node_value))


def write_value_bool(node_id, value):
    client_node = client.get_node(node_id)
    client_node_value = value

    client_node_dv = ua.DataValue(ua.Variant(client_node_value, ua.VariantType.Boolean))

    client_node.set_value(client_node_dv)

    # print("value of : " + str(client_node) + ' : ' + str(client_node_value))






