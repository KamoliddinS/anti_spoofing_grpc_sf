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
import PIL.Image

def get_image_from_path(path):
    image_array = cv2.imread(path)
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = PIL.Image.fromarray(image_array)
    image = image.tobytes()
    return image, image_array.shape[0], image_array.shape[1]



def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Will try to reszie image ...")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = my_pb2_grpc.ImageServiceStub(channel)
        image, height, width = get_image_from_path('test1.jpg')
        response = stub.ResizeImage(my_pb2.ImageRequest(image_data=image, height=height, width=width, quality=80))

        #save image
        image = PIL.Image.frombytes('RGB', (response.width_resized, response.height_resized), response.image_data_resized)
        # image = image.reshape((response.height, response.width, 3))
        image = np.array(image)
        cv2.imwrite('test1_resized.jpg', image)



        print("ImageService client received resized image ")

if __name__ == '__main__':
    logging.basicConfig()
    run()
