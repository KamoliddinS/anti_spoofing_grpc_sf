# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: my.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x08my.proto\x12\nhelloworld\"R\n\x0cImageRequest\x12\x12\n\nimage_data\x18\x01 \x01(\x0c\x12\r\n\x05width\x18\x02 \x01(\x05\x12\x0e\n\x06height\x18\x03 \x01(\x05\x12\x0f\n\x07quality\x18\x04 \x01(\x02\"Y\n\x0cResizedImage\x12\x1a\n\x12image_data_resized\x18\x01 \x01(\x0c\x12\x15\n\rwidth_resized\x18\x02 \x01(\x05\x12\x16\n\x0eheight_resized\x18\x03 \x01(\x05\x32S\n\x0cImageService\x12\x43\n\x0bResizeImage\x12\x18.helloworld.ImageRequest\x1a\x18.helloworld.ResizedImage\"\x00\x42\x36\n\x1bio.grpc.examples.helloworldB\x0fHelloWorldProtoP\x01\xa2\x02\x03HLWb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'my_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033io.grpc.examples.helloworldB\017HelloWorldProtoP\001\242\002\003HLW'
  _IMAGEREQUEST._serialized_start=24
  _IMAGEREQUEST._serialized_end=106
  _RESIZEDIMAGE._serialized_start=108
  _RESIZEDIMAGE._serialized_end=197
  _IMAGESERVICE._serialized_start=199
  _IMAGESERVICE._serialized_end=282
# @@protoc_insertion_point(module_scope)
