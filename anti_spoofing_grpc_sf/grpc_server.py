
from concurrent import futures
import logging

import grpc
import my_pb2
import my_pb2_grpc
import  cv2
import numpy as np
import PIL.Image as Image

def reduce_image_quality(image_data, width, height, quality):
    image = Image.frombytes('RGB', (width, height), image_data)
    scale_percent = quality  # percent of original size
    width_new = int(image.size[0] * scale_percent / 100)
    height_new = int(image.size[1] * scale_percent / 100)
    dim = (width_new, height_new)
    # resize image
    image = np.array(image)
    image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

    image = Image.fromarray(image)
    image = image.tobytes()
    return image , width_new, height_new
class ImageService(my_pb2_grpc.ImageServiceServicer):

    def ResizeImage(self, request, context):
        image, width, height = reduce_image_quality(request.image_data, request.width, request.height, request.quality)
        return my_pb2.ResizedImage(image_data_resized=image, width_resized=width, height_resized=height)






def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    my_pb2_grpc.add_ImageServiceServicer_to_server(ImageService(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()