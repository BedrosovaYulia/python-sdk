# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/iot/devices/v1/device_data_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/iot/devices/v1/device_data_service.proto',
  package='yandex.cloud.iot.devices.v1',
  syntax='proto3',
  serialized_options=b'\n\037yandex.cloud.api.iot.devices.v1ZGgithub.com/yandex-cloud/go-genproto/yandex/cloud/iot/devices/v1;devices',
  serialized_pb=b'\n5yandex/cloud/iot/devices/v1/device_data_service.proto\x12\x1byandex.cloud.iot.devices.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1dyandex/cloud/validation.proto\"v\n\x18PublishDeviceDataRequest\x12\x1f\n\tdevice_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\x05topic\x18\x02 \x01(\tB\x0e\xe8\xc7\x31\x01\x8a\xc8\x31\x06<=1024\x12\x1a\n\x04\x64\x61ta\x18\x03 \x01(\x0c\x42\x0c\x8a\xc8\x31\x08<=262144\"\x1b\n\x19PublishDeviceDataResponse2\xc6\x01\n\x11\x44\x65viceDataService\x12\xb0\x01\n\x07Publish\x12\x35.yandex.cloud.iot.devices.v1.PublishDeviceDataRequest\x1a\x36.yandex.cloud.iot.devices.v1.PublishDeviceDataResponse\"6\x82\xd3\xe4\x93\x02\x30\"+/iot-devices/v1/devices/{device_id}/publish:\x01*Bj\n\x1fyandex.cloud.api.iot.devices.v1ZGgithub.com/yandex-cloud/go-genproto/yandex/cloud/iot/devices/v1;devicesb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])




_PUBLISHDEVICEDATAREQUEST = _descriptor.Descriptor(
  name='PublishDeviceDataRequest',
  full_name='yandex.cloud.iot.devices.v1.PublishDeviceDataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_id', full_name='yandex.cloud.iot.devices.v1.PublishDeviceDataRequest.device_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='topic', full_name='yandex.cloud.iot.devices.v1.PublishDeviceDataRequest.topic', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\006<=1024', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='yandex.cloud.iot.devices.v1.PublishDeviceDataRequest.data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\010<=262144', file=DESCRIPTOR),
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
  serialized_start=147,
  serialized_end=265,
)


_PUBLISHDEVICEDATARESPONSE = _descriptor.Descriptor(
  name='PublishDeviceDataResponse',
  full_name='yandex.cloud.iot.devices.v1.PublishDeviceDataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=267,
  serialized_end=294,
)

DESCRIPTOR.message_types_by_name['PublishDeviceDataRequest'] = _PUBLISHDEVICEDATAREQUEST
DESCRIPTOR.message_types_by_name['PublishDeviceDataResponse'] = _PUBLISHDEVICEDATARESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PublishDeviceDataRequest = _reflection.GeneratedProtocolMessageType('PublishDeviceDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _PUBLISHDEVICEDATAREQUEST,
  '__module__' : 'yandex.cloud.iot.devices.v1.device_data_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iot.devices.v1.PublishDeviceDataRequest)
  })
_sym_db.RegisterMessage(PublishDeviceDataRequest)

PublishDeviceDataResponse = _reflection.GeneratedProtocolMessageType('PublishDeviceDataResponse', (_message.Message,), {
  'DESCRIPTOR' : _PUBLISHDEVICEDATARESPONSE,
  '__module__' : 'yandex.cloud.iot.devices.v1.device_data_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iot.devices.v1.PublishDeviceDataResponse)
  })
_sym_db.RegisterMessage(PublishDeviceDataResponse)


DESCRIPTOR._options = None
_PUBLISHDEVICEDATAREQUEST.fields_by_name['device_id']._options = None
_PUBLISHDEVICEDATAREQUEST.fields_by_name['topic']._options = None
_PUBLISHDEVICEDATAREQUEST.fields_by_name['data']._options = None

_DEVICEDATASERVICE = _descriptor.ServiceDescriptor(
  name='DeviceDataService',
  full_name='yandex.cloud.iot.devices.v1.DeviceDataService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=297,
  serialized_end=495,
  methods=[
  _descriptor.MethodDescriptor(
    name='Publish',
    full_name='yandex.cloud.iot.devices.v1.DeviceDataService.Publish',
    index=0,
    containing_service=None,
    input_type=_PUBLISHDEVICEDATAREQUEST,
    output_type=_PUBLISHDEVICEDATARESPONSE,
    serialized_options=b'\202\323\344\223\0020\"+/iot-devices/v1/devices/{device_id}/publish:\001*',
  ),
])
_sym_db.RegisterServiceDescriptor(_DEVICEDATASERVICE)

DESCRIPTOR.services_by_name['DeviceDataService'] = _DEVICEDATASERVICE

# @@protoc_insertion_point(module_scope)
