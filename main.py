from ultralytics import YOLO
from PIL import Image
import cv2
import argparse
from ocr import OCR_Pred





def load_model(model_name):
    #Model loading
    trained_model = YOLO(model_name)
    return trained_model

def run():
    #Load the model
    ap = argparse.ArgumentParser()
    ocr = OCR_Pred()
    ap.add_argument("-m","--model",help="Provied Trained Model Name")
    ap.add_argument('-i','--image',help="Image Source")
    argv = vars(ap.parse_args())
    trainedModel = load_model(argv["model"])
    print(argv["image"])
    img = cv2.imread(argv["image"])
    results = trainedModel.predict(source=img)
    for result in results:
        result = result.cpu()
        result = result.numpy()
        cords = result.boxes.xyxy.tolist()
        
        for cord in cords: 
            cropped_img = img[int(cord[1]):int(cord[3]),int(cord[0]):int(cord[2])]
            #cv2.imshow("Cropped img",cropped_img)
            #cv2.waitKey(200)
            
            print(ocr.img_to_char(cropped_img))
        #cv2.destroyAllWindows()


if __name__== "__main__":
    run()
