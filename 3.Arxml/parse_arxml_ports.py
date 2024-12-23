import xml.etree.ElementTree as ET
import yaml


def extract_port_info(root):
    port_info = []
    ns = {'autosar': 'http://autosar.org/schema/r4.0'}
    for component_type in root.findall('.//autosar:APPLICATION-SW-COMPONENT-TYPE', ns):
        print(component_type)
        component_name = component_type.find('SHORT-NAME').text
        for port in component_type.findall('.//P-PORT-PROTOTYPE'):
            port_name = port.find('SHORT-NAME').text
            provided_interface = port.find('PROVIDED-INTERFACE-TREF').attrib['DEST'].split('/')[-1]
            description = get_port_description(port_name)
            data_type = get_data_type(provided_interface)
            port_info.append({
                'component': component_name,
                'port': port_name,
                'description': description,
                'type': data_type
            })
        for port in component_type.findall('.//R-PORT-PROTOTYPE'):
            port_name = port.find('SHORT-NAME').text
            required_interface = port.find('REQUIRED-INTERFACE-TREF').attrib['DEST'].split('/')[-1]
            description = get_port_description(port_name)
            data_type = get_data_type(required_interface)
            port_info.append({
                'component': component_name,
                'port': port_name,
                'description': description,
                'type': data_type
            })
    print(port_info)
    return port_info


def get_port_description(port_name):
    descriptions = {
        'Pp_ASW2BSW_HWO_b_RlyPreCtrl': 'Asw发给Bsw的单体电压数据',
        'Pp_BSW2ASW_HWI_V_BattLv': 'Bsw发给Asw的12v蓄电池电压'
        # 根据实际情况补充更多端口描述
    }
    return descriptions.get(port_name, '')


def get_data_type(interface_name):
    data_types = {
        'Pi_M_HWO_b_RlyPreCtrl': 'boolean',
        'Pi_M_HWI_V_BattLv': 'uint16'
        # 根据实际情况补充更多数据类型
    }
    return data_types.get(interface_name, '')


def write_yaml(port_info, file_path):
    yaml_data = {'Values': {}}
    for info in port_info:
        yaml_data['Values'][info['port']] = {
            'description': info['description'],
            'type': info['type']
        }
    with open(file_path, 'w') as file:
        yaml.dump(yaml_data, file)


def write_markdown(port_info, file_path):
    with open(file_path, 'w') as file:
        file.write('# BSW\n\n')
        file.write('| Sender /Server | Receiver /Client | S_Trigger | R_Trigger | Port type | Element(Structure/Array/Value) | Data type |\n')
        file.write('| -------------- | ---------------- | --------- | --------- | --------- | ------------------------------ | --------- |\n')
        for info in port_info:
            file.write(f'| {info["component"]} | {"ASW" if info["component"] == "BSW" else "BSW"} | {"10ms" if "10ms" in info["port"] else ""} | {"R_Event" if "R_Event" in info["port"] else ""} | SR | {info["port"]} | {info["type"]} |\n')


if __name__ == '__main__':
    tree = ET.parse('swc.arxml')
    root = tree.getroot()

    port_info = extract_port_info(root)

    write_yaml(port_info, 'port_info.yaml')
    write_markdown(port_info, 'port_relation.md')