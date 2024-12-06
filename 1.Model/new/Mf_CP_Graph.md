# MRM_CP

| Sender /Server | Receiver /Client | S_Trigger | R_Trigger | Port type | Element(Structure/Array/Value) | Data type |
| -------------- | ---------------- | --------- | --------- | --------- | ------------------------------ | --------- |
| MRM_CP         | VSS_CP             | 100ms      | 100ms      | SR        | MrmState                       | Value     |

# VSS_CP

| Sender /Server | Receiver /Client | S_Trigger | R_Trigger | Port type | Element(Structure/Array/Value) | Data type |
| -------------- | ---------------- | --------- | --------- | --------- | ------------------------------ | --------- |
| VSS_CP         | MRM_CP    | 100ms      | 100ms      | SR        | EscState                       | Value     |