import tflite_runtime.interpreter as tflite
import cv2
import numpy as np

def create_category_index(label_path='label/labelmap.txt'):
    f = open(label_path)
    category_index = {}
    for i, val in enumerate(f):
        if i != 0:
            val = val[:-1]
            if val != '???':
                category_index.update({(i-1): {'id': (i-1), 'name': val}})
    f.close()
    return category_index

category = create_category_index()

def classification(img):

    interpreter = tflite.Interpreter("coco.tflite")
    interpreter.allocate_tensors()
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    img = cv2.imread(img)
    img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img_rgb = cv2.resize(img_rgb, (300,300), cv2.INTER_AREA)
    img_rgb = img_rgb.reshape([1, 300,300, 3])

    interpreter.set_tensor(input_details[0]['index'], img_rgb)
    interpreter.invoke()

    det_boxes = interpreter.get_tensor(output_details[0]['index'])
    det_classes = interpreter.get_tensor(output_details[1]['index'])[0]
    det_scores = interpreter.get_tensor(output_details[2]['index'])[0]
    output = []
    output.append(det_classes)
    output.append(det_boxes)
    output.append(det_scores)
    return output


def tweet(img):

    conv = classification(img)
    reco = []
    for obj in conv[0]:
        reco.append(category.get(obj).get("name"))
    obj = reco[0]
    score = int(conv[2][0]*100)
    tweet = "@Archillect "+str(obj) +" "+ str(score)+"%"
    return tweet


