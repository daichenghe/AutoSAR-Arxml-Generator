# /*
#  * @Author: junhao.bai
#  * @Date: 2023-11-27
#  * @Last Modified by:   junhao.bai
#  * @Last Modified time: 2024-1-15 16:17:50
#  */

from enum import Enum
import os
import uuid
from lxml import etree
import pandas as pd
from typing import List, Dict, Optional, Set, Tuple

from component_types.component_types import ComponentType
from component_types.pr_ports import (
    ArrayValueSpecification,
    Elements,
    Fields,
    Filter,
    InitValue,
    NumericalValueSpecification,
    OperationRef,
    RecordValueSpecification,
    Ports,
    RPortPrototype,
    PPortPrototype,
    RequiredInterfaceTref,
    ProvidedInterfaceTref,
    RequiredComSpecs,
    ProvidedComSpecs,
    NonQueuedReceiverComSpec,
    NonQueuedSenderComSpec,
    ServerComSpec,
    DataElementRef,
)
from component_types.ports_creator import create_ports_xml
from component_types.internal_behaviors_creator import create_internal_behaviors_xml
from component_types.internal_behaviors import (
    AccessedVariable,
    AutosarVariableIref,
    ContextRPortRef,
    DataIref,
    DataReceivePointByArguments,
    DataReceivedEvent,
    DataSendPoints,
    Events,
    InitEvent,
    InternalBehaviors,
    OperationIrefPPort,
    OpreationInvokedEvent,
    PortPrototypeRef,
    RunnableEntity,
    Runnables,
    SwcInternalBehavior,
    SynchronousServerCallPoint,
    TargetDataPrototypeRef,
    TimingEvent,
    VariableAccess,
    ServerCallPoints,
    OperationIref,
    TargetRequiredOperationRef,
)

from logger_config import logger


class CtApManager:
    def __init__(self, excel_path: str):
        if not (excel_path.endswith('.xlsx') or excel_path.endswith('.xls')):
            raise ValueError("Invalid file format. Only.xlsx and.xls files are supported.")
        
        try:
            self.df = pd.read_excel(excel_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {excel_path}")
        except pd.errors.ParserError:
            raise pd.errors.ParserError(f"Error parsing the Excel file: {excel_path}")
        
        self.basic_types = [
            "sint8",
            "uint8",
            "sint16",
            "uint16",
            "sint32",
            "sint64",
            "uint32",
            "uint64",
            "float32",
            "float64",
            "boolean",
        ]
        """初始化函数, 加载excel数据"""
        self.complete_df = self.df.copy()  # 用于存储完整的DataFrame, 用于生成依赖关系字典
        self.definitions = {"Value": {}, "Array": {}, "Structure": {}}  # 用于存储依赖关系字典
        self.parse_definitions()  # 解析DataFrame中定义的数据结构, 生成依赖关系字典。
        self.df = self.df.dropna(
            axis=0, how="any", subset=["Sender /Server"]
        )  # 去除Sender /Server为空的行的数据, 用于生成CtAp_M_XXXX字典
    def parse_definitions(self):
        """
        解析DataFrame中定义的数据结构, 生成依赖关系字典。
        """
        # 需要用到的列是：Element(Structure/Array/Value), Data type, Base Type, Signal, DLC, Initial value
        # 总共是三个字典, Value, Array, Structure
        # 1.1 Data type是Structure的行, 若Element(Structure/Array/Value)相同则说明是同一个结构体, Signal是结构体的成员变量
        # 1.2 Data type是Structure的行, 若Base Type不是基本类型, 则说明Signal是一个结构体或者数组, 需要递归的进行处理
        # 1.3 Data type是Structure的行, 若Base Type是基本类型, 则说明Signal是一个基本类型的值, 不需要递归的进行处理
        # 注意: 这里Element(Structure/Array/Value)相同的行, 可能会重复添加Signal, 需要使用set进行去重
        # 2.1 Data type是Array的行, 若Ease Type不是基本类型, 则说明这个数组的元素是一组结构体或者数组, 需要递归的进行处理
        # 2.2 Data type是Array的行, 若Base Type是基本类型, 则说明这个数组的元素是一组基本类型的值, 不需要递归的进行处理
        # 3.1 Date type是Value的行, Base Type只有可能是基本类型, 不需要递归的进行处理
        # 首先创建一个dataframe存储需要的列
        minimal_df = self.complete_df[
            [
                "Element(Structure/Array/Value)",
                "Data type",
                "Base Type",
                "Signal",
                "DLC",
                "Initial value",
            ]
        ]

        # 先建立所有Value、Array和Structure的框架
        for index, row in minimal_df.iterrows():
            element = row["Element(Structure/Array/Value)"]
            data_type = row["Data type"]
            if element not in self.definitions[data_type]:
                if (
                    data_type == "Value"
                ):  # Value类型的数据, Base Type只有可能是基本类型, 将其添加到Value字典中
                    self.definitions[data_type][element] = {
                        "type": row["Base Type"],
                        "initial_value": row["Initial value"],
                        "is_value": True,
                        "is_array": False,
                        "is_structure": False,
                    }
                else:  # Array和Structure类型的数据, Base Type可能是基本类型, 也可能是数组或者结构体, 先将其添加到字典中, 然后再进行处理
                    self.definitions[data_type][element] = {
                        "type": data_type,
                        "base_type": None
                        if data_type == "Structure"
                        else row["Base Type"],
                        "is_value": False,
                        "is_array": True if data_type == "Array" else False,
                        "is_structure": True if data_type == "Structure" else False,
                        "members": {} if data_type == "Structure" else None,
                        "dlc": None if data_type == "Structure" else int(row["DLC"]),
                        "initial_value": row["Initial value"],
                    }

        # 然后填充结构体和数组内部的详细信息
        for index, row in minimal_df.iterrows():
            element = row["Element(Structure/Array/Value)"]
            data_type = row["Data type"]
            base_type = row["Base Type"]
            if data_type == "Structure":
                if base_type not in self.basic_types:
                    # 如果Base Type不是基本类型, 则说明Signal是一个结构体或者数组, 需要递归的进行处理
                    self.definitions[data_type][element]["members"][row["Signal"]] = self.definitions[data_type][base_type]
                else:
                    # 如果Base Type是基本类型, 则说明Signal是一个基本类型的值, 不需要递归的进行处理
                    self.definitions[data_type][element]["members"][row["Signal"]] = {
                        "type": base_type,
                        "initial_value": row["Initial value"],
                        "is_value": True,
                        "is_array": False,
                        "is_structure": False,
                    }
            elif data_type == "Array":
                if base_type not in self.basic_types:
                    # 如果Base Type不是基本类型, 则说明这个数组的元素是一组结构体或者数组, 需要递归的进行处理
                    self.definitions[data_type][element]["members"] = self.definitions[data_type][base_type]
                else:
                    # 如果Base Type是基本类型, 则说明这个数组的元素是一组基本类型的值, 不需要递归的进行处理
                    self.definitions[data_type][element]["members"] = {
                        "type": base_type,
                        "initial_value": row["Initial value"],
                        "is_value": True,
                        "is_array": False,
                        "is_structure": False,
                    }
