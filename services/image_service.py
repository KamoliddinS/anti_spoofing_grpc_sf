import my_pb2
import my_pb2_grpc
from dotenv import load_dotenv
from minio import Minio
import os
import  cv2
import numpy as np
from PIL import Image
from io import BytesIO
from src.anti_spoof_predict import AntiSpoofPredict
from src.generate_patches import CropImage
load_dotenv()
MINIO_ACCESS_KEY = os.environ.get("MINIO_ACCESS_KEY")
MINIO_SECRET_KEY = os.environ.get("MINIO_SECRET_KEY")
MINIO_HOST = os.environ.get("MINIO_HOST")
BUCKET_TO_SAVE = os.environ.get("BUCKET_TO_SAVE")

min_io_client = Minio(
    MINIO_HOST,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=False,
)


model = AntiSpoofPredict(0)
model2 = AntiSpoofPredict(0)
image_cropper = CropImage()
model._load_model("resources/anti_spoof_models/2.7_80x80_MiniFASNetV2.pth")
model2._load_model("resources/anti_spoof_models/4_0_0_80x80_MiniFASNetV1SE.pth")



def check_spoofing(bucket_name: str, object_name: str):
    image = min_io_client.get_object(bucket_name, object_name)
    image = np.array(Image.open(image))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
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
    is_spoofed = False
    if label == 1:
        print("Image '{}' is Real Face. Score: {:.2f}.".format(object_name, value))
        result_text = "RealFace Score: {:.2f}".format(value)
        color = (255, 0, 0)
    else:
        is_spoofed = True
        print("Image '{}' is Fake Face. Score: {:.2f}.".format(object_name, value))
        result_text = "FakeFace Score: {:.2f}".format(value)
        color = (0, 0, 255)
    cv2.rectangle(
        image,
        (image_bbox[0], image_bbox[1]),
        (image_bbox[0] + image_bbox[2], image_bbox[1] + image_bbox[3]),
        color, 2)
    cv2.putText(
        image,
        result_text,
        (image_bbox[0], image_bbox[1] - 5),
        cv2.FONT_HERSHEY_COMPLEX, 0.5 * image.shape[0] / 1024, color)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # save the image to minio
    buffer = BytesIO()
    pil_image = Image.fromarray(image)
    pil_image.save(buffer, format="JPEG")
    buffer.seek(0)
    min_io_client.put_object(BUCKET_TO_SAVE, object_name, buffer, buffer.getbuffer().nbytes)
    return is_spoofed, value, BUCKET_TO_SAVE, object_name


class ImageService(my_pb2_grpc.ImageServiceServicer):
    def GetSpoofingResult(self, request, context):
        is_spoofed, score, bucket_name, object_name = check_spoofing(request.bucket_name, request.object_name)
        return my_pb2.SpoofingResult(is_spoofed=is_spoofed, score=score, bucket_name=bucket_name, object_name=object_name)
