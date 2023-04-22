# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import logging

import grpc
import my_pb2
import my_pb2_grpc
import cv2
import numpy as np
from PIL import Image
import io

def get_image_from_path(path):
    img = Image.open(path)
    buf = io.BytesIO()
    img.save(buf, format='JPEG')
    bytes_image = buf.getvalue()
    return bytes_image



def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.

    print("Will try to run image ...")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = my_pb2_grpc.ImageServiceStub(channel)
        image_data = get_image_from_path('test3.jpg')
        # response = stub.ResizeImage(my_pb2.ImageRequest(image_data=image_data, quality=80))


        # image = Image.open(io.BytesIO(response.image_data_resized))
        # image = np.array(image)
        # cv2.imwrite('test1_resized.jpg', image)

        response = stub.GetSpoofingResult(my_pb2.ImageRequest(image_data=image_data))
        print("ImageService client received:  " + str(response.is_spoofing ) + " " + str(response.confidence))


if __name__ == '__main__':
    logging.basicConfig()
    run()
