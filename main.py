from ultralytics import YOLO
from PIL import Image
import cv2
import argparse
from ocr import OCR_Pred
import time
import pytesseract
import pymongo



def load_model(model_name):
    #Model loading
    trained_model = YOLO(model_name)
    return trained_model

def run():
    myclient = pymongo.MongoClient("mongodb+srv://root:root@majorapp.tnk70j0.mongodb.net/?retryWrites=true&w=majority")
    mydb = myclient['mernapp']
    mycol = mydb['number_plate']
    #Load the model
    ap = argparse.ArgumentParser()
    ocr = OCR_Pred()
    ap.add_argument("-m","--model",help="Provied Trained Model Name")
    ap.add_argument('-l','--location',help="set location")
    argv = vars(ap.parse_args())
    trainedModel = load_model(argv["model"])
    cap = cv2.VideoCapture(0)
    final_result = {}
    while cap.isOpened():
        ret, img = cap.read()
        results = trainedModel.predict(source=img)
        for result in results:
            #result = result.cpu() working with raspberry
            result = result.numpy()
            cords = result.boxes.xyxy.tolist()       
            for cord in cords: 
                cropped_img = img[int(cord[1]):int(cord[3]),int(cord[0]):int(cord[2])]
            #cv2.imshow("Cropped img",cropped_img)
            #cv2.waitKey(200)
            
                number_plate = pytesseract.image_to_string(cropped_img, lang ='eng',config ='-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 --oem 3 --psm 6 ')
                print(number_plate)
                final_number = "".join(number_plate)
                print(final_number)
                if len(final_number)>=8:
                    final_result[time.ctime(time.time())] = final_number
                
            
        for k,v in final_result.items():
            _=mycol.insert_one({'number_plate':v,'time':k,'location': argv["location"]})
    
    cap.release()


if __name__== "__main__":
    run()
