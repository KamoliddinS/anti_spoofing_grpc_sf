
from concurrent import futures
import logging

import grpc
import my_pb2
import my_pb2_grpc
import  cv2
import numpy as np
from PIL import Image
import io
from src.anti_spoof_predict import AntiSpoofPredict
from src.generate_patches import CropImage

model = AntiSpoofPredict(0)
model2 = AntiSpoofPredict(0)
image_cropper = CropImage()
model._load_model("resources/anti_spoof_models/2.7_80x80_MiniFASNetV2.pth")
model2._load_model("resources/anti_spoof_models/4_0_0_80x80_MiniFASNetV1SE.pth")
def reduce_image_quality(image_data, quality):
    image = Image.open(io.BytesIO(image_data))
    image = np.array(image)
    print(image.shape)
    scale_percent = quality  # percent of original size
    width_new = int(image.shape[1] * scale_percent / 100)
    height_new = int(image.shape[0] * scale_percent / 100)
    dim = (width_new, height_new)
    # resize image

    image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    image = Image.fromarray(image)
    buf = io.BytesIO()
    image.save(buf, format='JPEG')
    image = buf.getvalue()
    return image


def check_image(image):
    image = Image.open(io.BytesIO(image))
    image = np.array(image)
    image_bbox = model.get_bbox(image)
    prediction = np.zeros((1, 3))
    param = {
        "org_img": image,
        "bbox": image_bbox,
        "scale": 2.7,
        "out_w": 80,
        "out_h": 80,
        "crop": True,
    }
    img = image_cropper.crop(**param)
    prediction += model.predict(img)

    param = {
        "org_img": image,
        "bbox": image_bbox,
        "scale": 4.0,
        "out_w": 80,
        "out_h": 80,
        "crop": True,
    }
    img = image_cropper.crop(**param)
    prediction += model2.predict(img)
    label = np.argmax(prediction)
    value = prediction[0][label] / 2

    if label == 1:
        return False, value
    else:
        return True, value



class ImageService(my_pb2_grpc.ImageServiceServicer):
    def ResizeImage(self, request, context):
        image= reduce_image_quality( image_data=request.image_data, quality=request.quality)
        return my_pb2.ResizedImage(image_data_resized=image)
    def GetSpoofingResult(self, request, context):
        is_spoofing, confidence = check_image(request.image_data)
        return my_pb2.SpoofingResult(is_spoofing=is_spoofing, confidence=confidence)




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