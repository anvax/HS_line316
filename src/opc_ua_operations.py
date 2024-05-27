from opcua import ua, Client

client = Client("opc.tcp://10.160.160.61:4840")


# reading value from opc server
def read_input_value(node_id):
    return client.get_node(node_id).get_value()


# writing int value to opc server
def write_value_int(node_id, value):
    client_node = client.get_node(node_id)
    client_node_value = value
    client_node_dv = ua.DataValue(ua.Variant(client_node_value, ua.VariantType.Int16))
    client_node.set_value(client_node_dv)


# writing bool value to opc server
def write_value_bool(node_id, value):
    client_node = client.get_node(node_id)
    client_node_value = value
    client_node_dv = ua.DataValue(ua.Variant(client_node_value, ua.VariantType.Boolean))
    client_node.set_value(client_node_dv)
