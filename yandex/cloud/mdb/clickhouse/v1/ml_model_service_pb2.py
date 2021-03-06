# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/clickhouse/v1/ml_model_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.mdb.clickhouse.v1 import ml_model_pb2 as yandex_dot_cloud_dot_mdb_dot_clickhouse_dot_v1_dot_ml__model__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/mdb/clickhouse/v1/ml_model_service.proto',
  package='yandex.cloud.mdb.clickhouse.v1',
  syntax='proto3',
  serialized_options=b'\n\"yandex.cloud.api.mdb.clickhouse.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/clickhouse/v1;clickhouse',
  serialized_pb=b'\n5yandex/cloud/mdb/clickhouse/v1/ml_model_service.proto\x12\x1eyandex.cloud.mdb.clickhouse.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\x1a-yandex/cloud/mdb/clickhouse/v1/ml_model.proto\"l\n\x11GetMlModelRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x35\n\rml_model_name\x18\x02 \x01(\tB\x1e\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=63\xf2\xc7\x31\x0e[a-zA-Z0-9_-]*\"u\n\x13ListMlModelsRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"k\n\x14ListMlModelsResponse\x12:\n\tml_models\x18\x01 \x03(\x0b\x32\'.yandex.cloud.mdb.clickhouse.v1.MlModel\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xc3\x01\n\x14\x43reateMlModelRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x35\n\rml_model_name\x18\x02 \x01(\tB\x1e\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=63\xf2\xc7\x31\x0e[a-zA-Z0-9_-]*\x12?\n\x04type\x18\x03 \x01(\x0e\x32+.yandex.cloud.mdb.clickhouse.v1.MlModelTypeB\x04\xe8\xc7\x31\x01\x12\x11\n\x03uri\x18\x04 \x01(\tB\x04\xe8\xc7\x31\x01\"B\n\x15\x43reateMlModelMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x15\n\rml_model_name\x18\x02 \x01(\t\"\xad\x01\n\x14UpdateMlModelRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x35\n\rml_model_name\x18\x02 \x01(\tB\x1e\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=63\xf2\xc7\x31\x0e[a-zA-Z0-9_-]*\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x0b\n\x03uri\x18\x04 \x01(\t\"B\n\x15UpdateMlModelMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x15\n\rml_model_name\x18\x02 \x01(\t\"o\n\x14\x44\x65leteMlModelRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x35\n\rml_model_name\x18\x02 \x01(\tB\x1e\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=63\xf2\xc7\x31\x0e[a-zA-Z0-9_-]*\"B\n\x15\x44\x65leteMlModelMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x15\n\rml_model_name\x18\x02 \x01(\t2\xff\x07\n\x0eMlModelService\x12\xb0\x01\n\x03Get\x12\x31.yandex.cloud.mdb.clickhouse.v1.GetMlModelRequest\x1a\'.yandex.cloud.mdb.clickhouse.v1.MlModel\"M\x82\xd3\xe4\x93\x02G\x12\x45/managed-clickhouse/v1/clusters/{cluster_id}/mlModels/{ml_model_name}\x12\xb0\x01\n\x04List\x12\x33.yandex.cloud.mdb.clickhouse.v1.ListMlModelsRequest\x1a\x34.yandex.cloud.mdb.clickhouse.v1.ListMlModelsResponse\"=\x82\xd3\xe4\x93\x02\x37\x12\x35/managed-clickhouse/v1/clusters/{cluster_id}/mlModels\x12\xc7\x01\n\x06\x43reate\x12\x34.yandex.cloud.mdb.clickhouse.v1.CreateMlModelRequest\x1a!.yandex.cloud.operation.Operation\"d\x82\xd3\xe4\x93\x02:\"5/managed-clickhouse/v1/clusters/{cluster_id}/mlModels:\x01*\xb2\xd2* \n\x15\x43reateMlModelMetadata\x12\x07MlModel\x12\xd7\x01\n\x06Update\x12\x34.yandex.cloud.mdb.clickhouse.v1.UpdateMlModelRequest\x1a!.yandex.cloud.operation.Operation\"t\x82\xd3\xe4\x93\x02J2E/managed-clickhouse/v1/clusters/{cluster_id}/mlModels/{ml_model_name}:\x01*\xb2\xd2* \n\x15UpdateMlModelMetadata\x12\x07MlModel\x12\xe2\x01\n\x06\x44\x65lete\x12\x34.yandex.cloud.mdb.clickhouse.v1.DeleteMlModelRequest\x1a!.yandex.cloud.operation.Operation\"\x7f\x82\xd3\xe4\x93\x02G*E/managed-clickhouse/v1/clusters/{cluster_id}/mlModels/{ml_model_name}\xb2\xd2*.\n\x15\x44\x65leteMlModelMetadata\x12\x15google.protobuf.EmptyBs\n\"yandex.cloud.api.mdb.clickhouse.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/clickhouse/v1;clickhouseb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,yandex_dot_cloud_dot_api_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_operation_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_mdb_dot_clickhouse_dot_v1_dot_ml__model__pb2.DESCRIPTOR,])




_GETMLMODELREQUEST = _descriptor.Descriptor(
  name='GetMlModelRequest',
  full_name='yandex.cloud.mdb.clickhouse.v1.GetMlModelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.clickhouse.v1.GetMlModelRequest.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ml_model_name', full_name='yandex.cloud.mdb.clickhouse.v1.GetMlModelRequest.ml_model_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=63\362\3071\016[a-zA-Z0-9_-]*', file=DESCRIPTOR),
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
  serialized_start=305,
  serialized_end=413,
)


_LISTMLMODELSREQUEST = _descriptor.Descriptor(
  name='ListMlModelsRequest',
  full_name='yandex.cloud.mdb.clickhouse.v1.ListMlModelsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.clickhouse.v1.ListMlModelsRequest.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='yandex.cloud.mdb.clickhouse.v1.ListMlModelsRequest.page_size', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\006<=1000', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='yandex.cloud.mdb.clickhouse.v1.ListMlModelsRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\005<=100', file=DESCRIPTOR),
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
  serialized_start=415,
  serialized_end=532,
)


_LISTMLMODELSRESPONSE = _descriptor.Descriptor(
  name='ListMlModelsResponse',
  full_name='yandex.cloud.mdb.clickhouse.v1.ListMlModelsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ml_models', full_name='yandex.cloud.mdb.clickhouse.v1.ListMlModelsResponse.ml_models', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='yandex.cloud.mdb.clickhouse.v1.ListMlModelsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=534,
  serialized_end=641,
)


_CREATEMLMODELREQUEST = _descriptor.Descriptor(
  name='CreateMlModelRequest',
  full_name='yandex.cloud.mdb.clickhouse.v1.CreateMlModelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.clickhouse.v1.CreateMlModelRequest.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ml_model_name', full_name='yandex.cloud.mdb.clickhouse.v1.CreateMlModelRequest.ml_model_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=63\362\3071\016[a-zA-Z0-9_-]*', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='yandex.cloud.mdb.clickhouse.v1.CreateMlModelRequest.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uri', full_name='yandex.cloud.mdb.clickhouse.v1.CreateMlModelRequest.uri', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001', file=DESCRIPTOR),
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
  serialized_start=644,
  serialized_end=839,
)


_CREATEMLMODELMETADATA = _descriptor.Descriptor(
  name='CreateMlModelMetadata',
  full_name='yandex.cloud.mdb.clickhouse.v1.CreateMlModelMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.clickhouse.v1.CreateMlModelMetadata.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ml_model_name', full_name='yandex.cloud.mdb.clickhouse.v1.CreateMlModelMetadata.ml_model_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=841,
  serialized_end=907,
)


_UPDATEMLMODELREQUEST = _descriptor.Descriptor(
  name='UpdateMlModelRequest',
  full_name='yandex.cloud.mdb.clickhouse.v1.UpdateMlModelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.clickhouse.v1.UpdateMlModelRequest.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ml_model_name', full_name='yandex.cloud.mdb.clickhouse.v1.UpdateMlModelRequest.ml_model_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=63\362\3071\016[a-zA-Z0-9_-]*', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='yandex.cloud.mdb.clickhouse.v1.UpdateMlModelRequest.update_mask', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uri', full_name='yandex.cloud.mdb.clickhouse.v1.UpdateMlModelRequest.uri', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=910,
  serialized_end=1083,
)


_UPDATEMLMODELMETADATA = _descriptor.Descriptor(
  name='UpdateMlModelMetadata',
  full_name='yandex.cloud.mdb.clickhouse.v1.UpdateMlModelMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.clickhouse.v1.UpdateMlModelMetadata.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ml_model_name', full_name='yandex.cloud.mdb.clickhouse.v1.UpdateMlModelMetadata.ml_model_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=1085,
  serialized_end=1151,
)


_DELETEMLMODELREQUEST = _descriptor.Descriptor(
  name='DeleteMlModelRequest',
  full_name='yandex.cloud.mdb.clickhouse.v1.DeleteMlModelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.clickhouse.v1.DeleteMlModelRequest.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ml_model_name', full_name='yandex.cloud.mdb.clickhouse.v1.DeleteMlModelRequest.ml_model_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=63\362\3071\016[a-zA-Z0-9_-]*', file=DESCRIPTOR),
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
  serialized_start=1153,
  serialized_end=1264,
)


_DELETEMLMODELMETADATA = _descriptor.Descriptor(
  name='DeleteMlModelMetadata',
  full_name='yandex.cloud.mdb.clickhouse.v1.DeleteMlModelMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.clickhouse.v1.DeleteMlModelMetadata.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ml_model_name', full_name='yandex.cloud.mdb.clickhouse.v1.DeleteMlModelMetadata.ml_model_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=1266,
  serialized_end=1332,
)

_LISTMLMODELSRESPONSE.fields_by_name['ml_models'].message_type = yandex_dot_cloud_dot_mdb_dot_clickhouse_dot_v1_dot_ml__model__pb2._MLMODEL
_CREATEMLMODELREQUEST.fields_by_name['type'].enum_type = yandex_dot_cloud_dot_mdb_dot_clickhouse_dot_v1_dot_ml__model__pb2._MLMODELTYPE
_UPDATEMLMODELREQUEST.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
DESCRIPTOR.message_types_by_name['GetMlModelRequest'] = _GETMLMODELREQUEST
DESCRIPTOR.message_types_by_name['ListMlModelsRequest'] = _LISTMLMODELSREQUEST
DESCRIPTOR.message_types_by_name['ListMlModelsResponse'] = _LISTMLMODELSRESPONSE
DESCRIPTOR.message_types_by_name['CreateMlModelRequest'] = _CREATEMLMODELREQUEST
DESCRIPTOR.message_types_by_name['CreateMlModelMetadata'] = _CREATEMLMODELMETADATA
DESCRIPTOR.message_types_by_name['UpdateMlModelRequest'] = _UPDATEMLMODELREQUEST
DESCRIPTOR.message_types_by_name['UpdateMlModelMetadata'] = _UPDATEMLMODELMETADATA
DESCRIPTOR.message_types_by_name['DeleteMlModelRequest'] = _DELETEMLMODELREQUEST
DESCRIPTOR.message_types_by_name['DeleteMlModelMetadata'] = _DELETEMLMODELMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetMlModelRequest = _reflection.GeneratedProtocolMessageType('GetMlModelRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETMLMODELREQUEST,
  '__module__' : 'yandex.cloud.mdb.clickhouse.v1.ml_model_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.clickhouse.v1.GetMlModelRequest)
  })
_sym_db.RegisterMessage(GetMlModelRequest)

ListMlModelsRequest = _reflection.GeneratedProtocolMessageType('ListMlModelsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTMLMODELSREQUEST,
  '__module__' : 'yandex.cloud.mdb.clickhouse.v1.ml_model_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.clickhouse.v1.ListMlModelsRequest)
  })
_sym_db.RegisterMessage(ListMlModelsRequest)

ListMlModelsResponse = _reflection.GeneratedProtocolMessageType('ListMlModelsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTMLMODELSRESPONSE,
  '__module__' : 'yandex.cloud.mdb.clickhouse.v1.ml_model_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.clickhouse.v1.ListMlModelsResponse)
  })
_sym_db.RegisterMessage(ListMlModelsResponse)

CreateMlModelRequest = _reflection.GeneratedProtocolMessageType('CreateMlModelRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEMLMODELREQUEST,
  '__module__' : 'yandex.cloud.mdb.clickhouse.v1.ml_model_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.clickhouse.v1.CreateMlModelRequest)
  })
_sym_db.RegisterMessage(CreateMlModelRequest)

CreateMlModelMetadata = _reflection.GeneratedProtocolMessageType('CreateMlModelMetadata', (_message.Message,), {
  'DESCRIPTOR' : _CREATEMLMODELMETADATA,
  '__module__' : 'yandex.cloud.mdb.clickhouse.v1.ml_model_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.clickhouse.v1.CreateMlModelMetadata)
  })
_sym_db.RegisterMessage(CreateMlModelMetadata)

UpdateMlModelRequest = _reflection.GeneratedProtocolMessageType('UpdateMlModelRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEMLMODELREQUEST,
  '__module__' : 'yandex.cloud.mdb.clickhouse.v1.ml_model_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.clickhouse.v1.UpdateMlModelRequest)
  })
_sym_db.RegisterMessage(UpdateMlModelRequest)

UpdateMlModelMetadata = _reflection.GeneratedProtocolMessageType('UpdateMlModelMetadata', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEMLMODELMETADATA,
  '__module__' : 'yandex.cloud.mdb.clickhouse.v1.ml_model_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.clickhouse.v1.UpdateMlModelMetadata)
  })
_sym_db.RegisterMessage(UpdateMlModelMetadata)

DeleteMlModelRequest = _reflection.GeneratedProtocolMessageType('DeleteMlModelRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEMLMODELREQUEST,
  '__module__' : 'yandex.cloud.mdb.clickhouse.v1.ml_model_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.clickhouse.v1.DeleteMlModelRequest)
  })
_sym_db.RegisterMessage(DeleteMlModelRequest)

DeleteMlModelMetadata = _reflection.GeneratedProtocolMessageType('DeleteMlModelMetadata', (_message.Message,), {
  'DESCRIPTOR' : _DELETEMLMODELMETADATA,
  '__module__' : 'yandex.cloud.mdb.clickhouse.v1.ml_model_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.clickhouse.v1.DeleteMlModelMetadata)
  })
_sym_db.RegisterMessage(DeleteMlModelMetadata)


DESCRIPTOR._options = None
_GETMLMODELREQUEST.fields_by_name['cluster_id']._options = None
_GETMLMODELREQUEST.fields_by_name['ml_model_name']._options = None
_LISTMLMODELSREQUEST.fields_by_name['cluster_id']._options = None
_LISTMLMODELSREQUEST.fields_by_name['page_size']._options = None
_LISTMLMODELSREQUEST.fields_by_name['page_token']._options = None
_CREATEMLMODELREQUEST.fields_by_name['cluster_id']._options = None
_CREATEMLMODELREQUEST.fields_by_name['ml_model_name']._options = None
_CREATEMLMODELREQUEST.fields_by_name['type']._options = None
_CREATEMLMODELREQUEST.fields_by_name['uri']._options = None
_UPDATEMLMODELREQUEST.fields_by_name['cluster_id']._options = None
_UPDATEMLMODELREQUEST.fields_by_name['ml_model_name']._options = None
_DELETEMLMODELREQUEST.fields_by_name['cluster_id']._options = None
_DELETEMLMODELREQUEST.fields_by_name['ml_model_name']._options = None

_MLMODELSERVICE = _descriptor.ServiceDescriptor(
  name='MlModelService',
  full_name='yandex.cloud.mdb.clickhouse.v1.MlModelService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1335,
  serialized_end=2358,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='yandex.cloud.mdb.clickhouse.v1.MlModelService.Get',
    index=0,
    containing_service=None,
    input_type=_GETMLMODELREQUEST,
    output_type=yandex_dot_cloud_dot_mdb_dot_clickhouse_dot_v1_dot_ml__model__pb2._MLMODEL,
    serialized_options=b'\202\323\344\223\002G\022E/managed-clickhouse/v1/clusters/{cluster_id}/mlModels/{ml_model_name}',
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='yandex.cloud.mdb.clickhouse.v1.MlModelService.List',
    index=1,
    containing_service=None,
    input_type=_LISTMLMODELSREQUEST,
    output_type=_LISTMLMODELSRESPONSE,
    serialized_options=b'\202\323\344\223\0027\0225/managed-clickhouse/v1/clusters/{cluster_id}/mlModels',
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='yandex.cloud.mdb.clickhouse.v1.MlModelService.Create',
    index=2,
    containing_service=None,
    input_type=_CREATEMLMODELREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002:\"5/managed-clickhouse/v1/clusters/{cluster_id}/mlModels:\001*\262\322* \n\025CreateMlModelMetadata\022\007MlModel',
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='yandex.cloud.mdb.clickhouse.v1.MlModelService.Update',
    index=3,
    containing_service=None,
    input_type=_UPDATEMLMODELREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002J2E/managed-clickhouse/v1/clusters/{cluster_id}/mlModels/{ml_model_name}:\001*\262\322* \n\025UpdateMlModelMetadata\022\007MlModel',
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='yandex.cloud.mdb.clickhouse.v1.MlModelService.Delete',
    index=4,
    containing_service=None,
    input_type=_DELETEMLMODELREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002G*E/managed-clickhouse/v1/clusters/{cluster_id}/mlModels/{ml_model_name}\262\322*.\n\025DeleteMlModelMetadata\022\025google.protobuf.Empty',
  ),
])
_sym_db.RegisterServiceDescriptor(_MLMODELSERVICE)

DESCRIPTOR.services_by_name['MlModelService'] = _MLMODELSERVICE

# @@protoc_insertion_point(module_scope)
