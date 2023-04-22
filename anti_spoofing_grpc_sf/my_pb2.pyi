from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ImageRequest(_message.Message):
    __slots__ = ["height", "image_data", "quality", "width"]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_DATA_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    height: int
    image_data: bytes
    quality: float
    width: int
    def __init__(self, image_data: _Optional[bytes] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., quality: _Optional[float] = ...) -> None: ...

class ResizedImage(_message.Message):
    __slots__ = ["height_resized", "image_data_resized", "width_resized"]
    HEIGHT_RESIZED_FIELD_NUMBER: _ClassVar[int]
    IMAGE_DATA_RESIZED_FIELD_NUMBER: _ClassVar[int]
    WIDTH_RESIZED_FIELD_NUMBER: _ClassVar[int]
    height_resized: int
    image_data_resized: bytes
    width_resized: int
    def __init__(self, image_data_resized: _Optional[bytes] = ..., width_resized: _Optional[int] = ..., height_resized: _Optional[int] = ...) -> None: ...
