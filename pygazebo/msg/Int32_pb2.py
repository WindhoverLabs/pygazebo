# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Int32.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Int32.proto',
  package='std_msgs.msgs',
  serialized_pb=_b('\n\x0bInt32.proto\x12\rstd_msgs.msgs\"\x15\n\x05Int32\x12\x0c\n\x04\x64\x61ta\x18\x01 \x02(\x05')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_INT32 = _descriptor.Descriptor(
  name='Int32',
  full_name='std_msgs.msgs.Int32',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='std_msgs.msgs.Int32.data', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=51,
)

DESCRIPTOR.message_types_by_name['Int32'] = _INT32

Int32 = _reflection.GeneratedProtocolMessageType('Int32', (_message.Message,), dict(
  DESCRIPTOR = _INT32,
  __module__ = 'Int32_pb2'
  # @@protoc_insertion_point(class_scope:std_msgs.msgs.Int32)
  ))
_sym_db.RegisterMessage(Int32)


# @@protoc_insertion_point(module_scope)