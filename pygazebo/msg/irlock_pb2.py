# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: irlock.proto

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
  name='irlock.proto',
  package='irlock_msgs.msgs',
  serialized_pb=_b('\n\x0cirlock.proto\x12\x10irlock_msgs.msgs\"l\n\x06irlock\x12\x11\n\ttime_usec\x18\x01 \x02(\x02\x12\x11\n\tsignature\x18\x02 \x02(\x05\x12\r\n\x05pos_x\x18\x03 \x02(\x02\x12\r\n\x05pos_y\x18\x04 \x02(\x02\x12\x0e\n\x06size_x\x18\x05 \x02(\x02\x12\x0e\n\x06size_y\x18\x06 \x02(\x02')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_IRLOCK = _descriptor.Descriptor(
  name='irlock',
  full_name='irlock_msgs.msgs.irlock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time_usec', full_name='irlock_msgs.msgs.irlock.time_usec', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature', full_name='irlock_msgs.msgs.irlock.signature', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pos_x', full_name='irlock_msgs.msgs.irlock.pos_x', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pos_y', full_name='irlock_msgs.msgs.irlock.pos_y', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='size_x', full_name='irlock_msgs.msgs.irlock.size_x', index=4,
      number=5, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='size_y', full_name='irlock_msgs.msgs.irlock.size_y', index=5,
      number=6, type=2, cpp_type=6, label=2,
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
  serialized_start=34,
  serialized_end=142,
)

DESCRIPTOR.message_types_by_name['irlock'] = _IRLOCK

irlock = _reflection.GeneratedProtocolMessageType('irlock', (_message.Message,), dict(
  DESCRIPTOR = _IRLOCK,
  __module__ = 'irlock_pb2'
  # @@protoc_insertion_point(class_scope:irlock_msgs.msgs.irlock)
  ))
_sym_db.RegisterMessage(irlock)


# @@protoc_insertion_point(module_scope)