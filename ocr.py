

import cv2
import json
from torchvision import models
from easyocr import Reader
class OCR_Pred:

    def __init__(self):
        self.model = Reader(['en'],gpu=True)

    def img_to_char(self,img):
        result = self.model.readtext(img)
        ans = ""
        return ans
        
