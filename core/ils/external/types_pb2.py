# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: core/ils/external/types.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x63ore/ils/external/types.proto\x12\x17neoception.ils.external\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/protobuf/struct.proto*`\n\x11\x43\x61rrierActionType\x12\x1a\n\x16\x43\x41RRIER_ACTION_UNKNOWN\x10\x00\x12\x16\n\x12\x43\x41RRIER_ACTION_PUT\x10\x01\x12\x17\n\x13\x43\x41RRIER_ACTION_PICK\x10\x02*R\n\x0cLocationType\x12\x14\n\x10LOCATION_UNKNOWN\x10\x00\x12\x14\n\x10LOCATION_PRIMARY\x10\x01\x12\x16\n\x12LOCATION_SECONDARY\x10\x02\x42~\n\x1b\x63om.neoception.ils.externalB\rIlsEventTypesP\x01Z;gitlab.com/neoception/products/interfaces/core/ils/external\xaa\x02\x10Neo.Ils.Externalb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'core.ils.external.types_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033com.neoception.ils.externalB\rIlsEventTypesP\001Z;gitlab.com/neoception/products/interfaces/core/ils/external\252\002\020Neo.Ils.External'
  _CARRIERACTIONTYPE._serialized_start=121
  _CARRIERACTIONTYPE._serialized_end=217
  _LOCATIONTYPE._serialized_start=219
  _LOCATIONTYPE._serialized_end=301
# @@protoc_insertion_point(module_scope)
