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
import time
import grpc
import my_pb2
import my_pb2_grpc

BUCKET_NAME = "tempobjects"
OBJECT_NAME = "test1.jpg"




def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = my_pb2_grpc.ImageServiceStub(channel)
        print("ImageService client created")
        test_speed = 0
        start_time = time.time()
        for i in range(1, 1000):
            response = stub.GetSpoofingResult(my_pb2.ImageRequest(bucket_name=BUCKET_NAME, object_name=OBJECT_NAME))
            print("ImageService client received: Is   " + str(response.is_spoofed) + " " + str(
                response.score) + " " + str(response.bucket_name) + " " + str(response.object_name))
        test_speed += time.time() - start_time
        print("Test speed for 1000: " + str(test_speed))

if __name__ == '__main__':
    logging.basicConfig()
    run()
