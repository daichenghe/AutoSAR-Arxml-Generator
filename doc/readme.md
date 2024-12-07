在 AUTOSAR（汽车开放系统架构）中，Properties name、Interface name、Data name 分别表示不同的概念，它们在 AUTOSAR 的架构中扮演着重要的角色。

### Properties name（属性名称）

在 AUTOSAR 中，属性（Properties）是用来描述软件组件（SWC）、接口（Interface）、数据类型（Data Type）等元素的特性的。属性名称（Properties name）是用来标识这些特性的名称，例如，一个数据类型的属性可能包括数据长度、数据类型、数据范围等。

### Interface name（接口名称）

接口（Interface）是 AUTOSAR 中用于定义软件组件之间或软件组件与硬件之间通信的机制。接口名称（Interface name）是用来标识不同类型接口的名称，例如，发送-接收接口（Sender-Receiver Interface）、客户端-服务器接口（Client-Server Interface）等。

### Data name（数据名称）

在 AUTOSAR 中，数据（Data）是通过接口在软件组件之间或软件组件与硬件之间传输的信息。数据名称（Data name）是用来标识这些数据的名称，例如，一个信号（Signal）或参数（Parameter）的名称。

这些名称和引用在 AUTOSAR 的配置和通信中起到了关键的作用，确保了不同组件和模块之间的正确交互和理解。


# Note
1. 修改 initial_value 为 excel 表的 init value
2. 增加连接：
```
        for short_name, ports_data in result_dict.items():
            # for rport, port_info in ports_data.get("rports", []).items():
            #     print(port_info)
            r_port_prototype_list = [
                RPortPrototype(
                    UUID=uuid.uuid4().hex.upper(),
                    short_name=str(rport),
                    required_interface_tref=RequiredInterfaceTref(
                        dest="SENDER-RECEIVER-INTERFACE",
                        value=f"/PortInterfaces/{port_info['interface_name']}",
                    ),
                    required_com_specs=RequiredComSpecs(
                        nonqueued_receiver_com_spec=NonQueuedReceiverComSpec(
                            uses_end_to_end_protection=False,  # 是否使用端到端保护, 默认为False
                            filter=Filter("ALWAYS"),  # 过滤器, 默认为ALWAYS
                            data_element_ref = DataElementRef(
                                dest="VARIABLE-DATA-PROTOTYPE",
                                value=f"/PortInterfaces/{port_info['interface_name']}/{port_info['element_name']}",
                            ),
                        )
                    ),
                )
                for rport, port_info in ports_data.get("rports", []).items()
            ]
```