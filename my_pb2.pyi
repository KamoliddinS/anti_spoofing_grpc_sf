from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ImageRequest(_message.Message):
    __slots__ = ["bucket_name", "object_name"]
    BUCKET_NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    bucket_name: str
    object_name: str
    def __init__(self, bucket_name: _Optional[str] = ..., object_name: _Optional[str] = ...) -> None: ...

class SpoofingResult(_message.Message):
    __slots__ = ["bucket_name", "is_spoofed", "object_name", "score"]
    BUCKET_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_SPOOFED_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    bucket_name: str
    is_spoofed: bool
    object_name: str
    score: float
    def __init__(self, is_spoofed: bool = ..., score: _Optional[float] = ..., bucket_name: _Optional[str] = ..., object_name: _Optional[str] = ...) -> None: ...
