# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/iam/v1/awscompatibility/access_key.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/iam/v1/awscompatibility/access_key.proto',
  package='yandex.cloud.iam.v1.awscompatibility',
  syntax='proto3',
  serialized_options=b'\n(yandex.cloud.api.iam.v1.awscompatibilityZYgithub.com/yandex-cloud/go-genproto/yandex/cloud/iam/v1/awscompatibility;awscompatibility',
  serialized_pb=b'\n5yandex/cloud/iam/v1/awscompatibility/access_key.proto\x12$yandex.cloud.iam.v1.awscompatibility\x1a\x1fgoogle/protobuf/timestamp.proto\"\x88\x01\n\tAccessKey\x12\n\n\x02id\x18\x01 \x01(\t\x12\x1a\n\x12service_account_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x0e\n\x06key_id\x18\x05 \x01(\tB\x85\x01\n(yandex.cloud.api.iam.v1.awscompatibilityZYgithub.com/yandex-cloud/go-genproto/yandex/cloud/iam/v1/awscompatibility;awscompatibilityb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_ACCESSKEY = _descriptor.Descriptor(
  name='AccessKey',
  full_name='yandex.cloud.iam.v1.awscompatibility.AccessKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.iam.v1.awscompatibility.AccessKey.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service_account_id', full_name='yandex.cloud.iam.v1.awscompatibility.AccessKey.service_account_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.iam.v1.awscompatibility.AccessKey.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.iam.v1.awscompatibility.AccessKey.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key_id', full_name='yandex.cloud.iam.v1.awscompatibility.AccessKey.key_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=265,
)

_ACCESSKEY.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['AccessKey'] = _ACCESSKEY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AccessKey = _reflection.GeneratedProtocolMessageType('AccessKey', (_message.Message,), {
  'DESCRIPTOR' : _ACCESSKEY,
  '__module__' : 'yandex.cloud.iam.v1.awscompatibility.access_key_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iam.v1.awscompatibility.AccessKey)
  })
_sym_db.RegisterMessage(AccessKey)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
