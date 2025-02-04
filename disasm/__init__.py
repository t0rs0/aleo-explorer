# Temporary dumping ground for tool functions

from node.types import *

def plaintext_type_to_str(value: PlaintextType):
    match value.type:
        case PlaintextType.Type.Literal:
            value: LiteralPlaintextType
            return value.literal_type.name.lower()
        case PlaintextType.Type.Interface:
            value: InterfacePlaintextType
            return str(value.interface)


def valuetype_to_mode_type_str(value: ValueType):
    mode = value.type.name.lower()
    if "record" in mode:
        mode = "private"
    match value.type:
        case ValueType.Type.Constant | ValueType.Type.Public | ValueType.Type.Private:
            # noinspection PyUnresolvedReferences
            t = plaintext_type_to_str(value.plaintext_type)
        case ValueType.Type.Record:
            value: RecordValueType
            t = str(value.identifier)
        case ValueType.Type.ExternalRecord:
            value: ExternalRecordValueType
            t = str(value.locator)
    return mode, t