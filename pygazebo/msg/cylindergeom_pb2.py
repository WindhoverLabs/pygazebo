# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='cylindergeom.proto',
  package='gazebo.msgs',
  serialized_pb='\n\x12\x63ylindergeom.proto\x12\x0bgazebo.msgs\".\n\x0c\x43ylinderGeom\x12\x0e\n\x06radius\x18\x01 \x02(\x01\x12\x0e\n\x06length\x18\x02 \x02(\x01')




_CYLINDERGEOM = descriptor.Descriptor(
  name='CylinderGeom',
  full_name='gazebo.msgs.CylinderGeom',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='radius', full_name='gazebo.msgs.CylinderGeom.radius', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='length', full_name='gazebo.msgs.CylinderGeom.length', index=1,
      number=2, type=1, cpp_type=5, label=2,
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
  serialized_start=35,
  serialized_end=81,
)

DESCRIPTOR.message_types_by_name['CylinderGeom'] = _CYLINDERGEOM

class CylinderGeom(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CYLINDERGEOM
  
  # @@protoc_insertion_point(class_scope:gazebo.msgs.CylinderGeom)

# @@protoc_insertion_point(module_scope)