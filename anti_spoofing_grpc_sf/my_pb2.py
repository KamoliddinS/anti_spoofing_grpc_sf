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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x08my.proto\x12\nhelloworld\"8\n\x0cImageRequest\x12\x13\n\x0b\x62ucket_name\x18\x01 \x01(\t\x12\x13\n\x0bobject_name\x18\x02 \x01(\t\"]\n\x0eSpoofingResult\x12\x12\n\nis_spoofed\x18\x01 \x01(\x08\x12\r\n\x05score\x18\x02 \x01(\x02\x12\x13\n\x0b\x62ucket_name\x18\x03 \x01(\t\x12\x13\n\x0bobject_name\x18\x04 \x01(\t2[\n\x0cImageService\x12K\n\x11GetSpoofingResult\x12\x18.helloworld.ImageRequest\x1a\x1a.helloworld.SpoofingResult\"\x00\x42\x36\n\x1bio.grpc.examples.helloworldB\x0fHelloWorldProtoP\x01\xa2\x02\x03HLWb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'my_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033io.grpc.examples.helloworldB\017HelloWorldProtoP\001\242\002\003HLW'
  _IMAGEREQUEST._serialized_start=24
  _IMAGEREQUEST._serialized_end=80
  _SPOOFINGRESULT._serialized_start=82
  _SPOOFINGRESULT._serialized_end=175
  _IMAGESERVICE._serialized_start=177
  _IMAGESERVICE._serialized_end=268
# @@protoc_insertion_point(module_scope)
