from utils.session import Session
from PIL import Image
import cv2, numpy as np
from io import BytesIO


def callback(data, connection):
    image = Image.open(BytesIO(data))
    image = cv2.cvtColor(np.asarray(image), cv2.COLOR_RGB2BGR)
    print("显示一帧图像")


if __name__ == "__main__":
    session = Session(host='172.17.0.17', port=1024, callback=callback)
