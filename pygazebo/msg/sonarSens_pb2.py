# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sonarSens.proto

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
  name='sonarSens.proto',
  package='sonarSens_msgs.msgs',
  serialized_pb=_b('\n\x0fsonarSens.proto\x12\x13sonarSens_msgs.msgs\"d\n\tsonarSens\x12\x11\n\ttime_msec\x18\x01 \x02(\x02\x12\x14\n\x0cmin_distance\x18\x02 \x02(\x02\x12\x14\n\x0cmax_distance\x18\x03 \x02(\x02\x12\x18\n\x10\x63urrent_distance\x18\x04 \x02(\x02')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SONARSENS = _descriptor.Descriptor(
  name='sonarSens',
  full_name='sonarSens_msgs.msgs.sonarSens',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time_msec', full_name='sonarSens_msgs.msgs.sonarSens.time_msec', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_distance', full_name='sonarSens_msgs.msgs.sonarSens.min_distance', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_distance', full_name='sonarSens_msgs.msgs.sonarSens.max_distance', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_distance', full_name='sonarSens_msgs.msgs.sonarSens.current_distance', index=3,
      number=4, type=2, cpp_type=6, label=2,
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
  serialized_start=40,
  serialized_end=140,
)

DESCRIPTOR.message_types_by_name['sonarSens'] = _SONARSENS

sonarSens = _reflection.GeneratedProtocolMessageType('sonarSens', (_message.Message,), dict(
  DESCRIPTOR = _SONARSENS,
  __module__ = 'sonarSens_pb2'
  # @@protoc_insertion_point(class_scope:sonarSens_msgs.msgs.sonarSens)
  ))
_sym_db.RegisterMessage(sonarSens)


# @@protoc_insertion_point(module_scope)