
from doctr.models import ocr_predictor
import cv2
import json
from torchvision import models
from easyocr import Reader
class OCR_Pred:

    def __init__(self):
        self.model = Reader(['en'],gpu=True)

    def img_to_char(self,img):
        result = self.model.readtext(img)
        print(result)
        ans = ""
        '''
        for page in result["pages"]:
            for block in page["blocks"]:
                for line in block['lines']:
                    for word in line['words']:
                        ans += word['value']
        '''
            
        return ans
        
