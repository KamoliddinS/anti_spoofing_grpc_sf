from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ImageRequest(_message.Message):
    __slots__ = ["image_data", "quality"]
    IMAGE_DATA_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    image_data: bytes
    quality: float
    def __init__(self, image_data: _Optional[bytes] = ..., quality: _Optional[float] = ...) -> None: ...

class ResizedImage(_message.Message):
    __slots__ = ["image_data_resized"]
    IMAGE_DATA_RESIZED_FIELD_NUMBER: _ClassVar[int]
    image_data_resized: bytes
    def __init__(self, image_data_resized: _Optional[bytes] = ...) -> None: ...

class SpoofingResult(_message.Message):
    __slots__ = ["confidence", "is_spoofing"]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    IS_SPOOFING_FIELD_NUMBER: _ClassVar[int]
    confidence: float
    is_spoofing: bool
    def __init__(self, is_spoofing: bool = ..., confidence: _Optional[float] = ...) -> None: ...
