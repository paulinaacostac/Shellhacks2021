#print obj count, labels, bounding boxes and accuracy
import pdb
import csv
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
import inference
import pickle
import numpy as np
import cv2
#import tensorflow as tf
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
from collections import defaultdict


import flask
from flask import Flask, jsonify, request 

# if tf.executing_eagerly():
#    tf.compat.v1.disable_eager_execution()
import hparams_config
import PIL
from PIL import Image
from pathlib import Path
from visualize import vis_utils
from keras import label_util
import matplotlib.pyplot as plt
# raspberrypi commands
# from gpiozero import LED
# from gpiozero.pins.pigpio import PiGPIOFactory
# from time import sleep
from threading import  Thread

# factory = PiGPIOFactory(host='192.168.4.1') #Raspberry Pi IP address
# right_heptic = LED(17, pin_factory=factory) 
# left_heptic = LED(27, pin_factory=factory)

objectID = 0
image_id = 0

label = ""

class Furkan:

    def __init__(self,img_id, image_number, boxes, classes, scores, labels, img, pickle_path='data.bin'):
        self.img_id = img_id
        self.image_number = image_number
        self.boxes = boxes
        self.classes = classes
        self.scores = scores
        self.labels = labels
        self.img = img
        self.model = self.load_model(pickle_path)

    # creating picStatsie
    def load_model(pickle_path):
        if os.path.isfile(pickle_path):
            with open(pickle_path, 'rb') as f:
                random_forest_model = pickle.load(f)
        else:
            #todo train
            return
        return random_forest_model

    def for_Furkan(self):
        #ymin, xmin, ymax, xmax
      print("for_Furkan running")
      i = 0
      global objectID

      id_count = 0
      dict = {}
      field_name = ["image_name", "image_id", "objectID", "class_number", "class_name",  "y_min", "x_min", "y_max", "x_max",  "accuracy", "distance_pred"]

      #adding to dictionary
    #   print("LEN of SCORES >>>> " + str(len(self.scores)))
      while i < len(self.scores):
        #   print(i)
          if self.scores[i] >= 0.6:
              y_min = self.boxes[i][0]
              x_min = self.boxes[i][1]
              y_max = self.boxes[i][2]
              x_max = self.boxes[i][3]
              certainty = self.scores[i]        #percentage of detection confidence
              class_number = self.classes[i]    #label for the type of object detected (ex '1' is the label  for 'human')
              class_name = self.labels.get(class_number)    #name of object detected (ex: 'human', 'chair', etc)

            # random forest model to predict distance based on coordinates, certainty, and class num  
              distance_pred = self.model.predict([[y_min, x_min, y_max , x_max, certainty, class_number]]) #predictors = ['y_min', 'x_min', 'y_max', 'x_max','prediction', 'class_number']
            #   print("DISTANCE PREDICTION >>>>>>>>>>", distance_pred)
              dictionary_entry = {
                                    "image_name": self.image_number, 
                                    "image_id": self.img_id, 
                                    "objectID": objectID, 
                                    "class_number": class_number,
                                    "class_name": class_name, 
                                    "y_min": int(y_min), 
                                    "x_min": int(x_min), 
                                    "y_max": int(y_max), 
                                    "x_max": int(x_max), 
                                    "accuracy": certainty,
                                    "distance_pred": distance_pred
                                }
              #dict.update(dictionary_entry)
              with open('out.csv', 'a') as csvfile:
                  writer = csv.DictWriter(csvfile, fieldnames = field_name)
                 # writer.writeheader()
                  writer.writerow(dictionary_entry)
                  print("writing dict to .csv = " + str(dictionary_entry))
              objectID += 1
        #   else:
        #       print("certainty score not high enough")

          i += 1

      return dict

    # transfering dictionary key/value onto CSV file
    def toCSV(self, dict):
        print("toCSV running")
        with open('out.csv', 'a', newline='') as t:
            thewriter = csv.writer(t)
            for key, value in dict.items():
                thewriter.writerow([key, value])
            # print("writing dict to .csv = " + str(dict))
            t.close()

class det_model:

    def __init__(self, model_file_name = 'efficientdet-d5'):
        print("det_model __init__ running")
        global image_id
        self.sess = self.load_session(model_file_name)


    def load_session(model_path):
        with tf.Session() as sess:
            tf.saved_model.load(sess, ['serve'], model_path)
            
            return sess 

    def detect_objcts(img):
        if isinstance(img, str):
            img = np.array(PIL.Image.open(f))

        detections = sess.run('detections:0', {'image_arrays:0': [img]})
        return detections

        files = list(Path('./data_pics/DataSet5').rglob('*.png'))
        params = inference.hparams_config.get_detection_config('efficientdet-d5').as_dict()
        label_map = params.get('label_map', None)

        with tf.Session() as sess:
            tf.saved_model.load(sess, ['serve'], './efficientdet-d5')
            raw_images = []
            for f in tf.io.gfile.glob('./data_pics/Dataset1/*.jpg'):
                raw_images.append(np.array(PIL.Image.open(f)))
            # driver = inference.ServingDriver('efficientdet-d5', './efficientdet-d5', min_score_thresh=0.6)
            for ind, ff in enumerate(files):
                # print("INDEX >>> " + str(ind))
                img_name = os.path.basename(ff)
                detections = sess.run('detections:0', {'image_arrays:0': [raw_images[ind]]})
                up_img = inference.visualize_image_prediction(ind, img_name, raw_images[ind], detections[0], label_map=label_map, min_score_thresh=0.6)
                image_id += 1
                # pdb.set_trace()
                # saving output
                PIL.Image.fromarray(up_img).save('./data_pics/D4&5_processed/' + img_name)

def right_alert():
    print("go right")

def left_alert():
    print("go left")

def right_left_alert():
    print("go back")

label_map = label_util.get_label_map('coco')


def give_directions(boxes, classes, scores, distances):
    # cd Desktop/REU_SUMMER21/automl/efficientdet
    # python3 pic_processor.py
        # label_map = label_util.get_label_map('coco')
        # print("label_map ", label_map)
        print("\n\n******new image processed*****")

        personCounter = 0
        personCounter6feet = 0
        objDic = defaultdict(default_factory)
        detectedRight = False
        detectedLeft = False
        detectedFront=False


        for ind, [y_min, x_min, y_max, x_max] in enumerate(boxes):
            obj_label = label_map.get(classes[ind])                
            print("object: ", obj_label)
            print("coordinates: ", y_min, x_min, y_max, x_max)
            if (float(distances[ind]) < 72):
                # print(distances[ind])
                if ((float(y_max) > 1.5 * float(x_min)) and (float(y_max) > (-1.5)* (float(x_max)) + 960)):
                    print("a(n) "+ obj_label + " detected in front")
                    detectedFront = True
                    #rlAlert = Thread(target=right_left_alert) 
                    #rlAlert.start()              
                elif (float(y_max) > 1.5 * float(x_max)):
                    print("a(n) "+ obj_label + " detected in front on left")
                    detectedLeft = True
                    #leftAlert = Thread(target=left_alert)
                    #leftAlert.start()
                elif (float(y_max) > (-1.5)* (float(x_min)) + 960):
                    print("a(n) "+ obj_label + " detected in front on right")
                    detectedRight = True
                    #rightAlert = Thread(target=right_alert)
                    #rightAlert.start()
            else:
                print("path clear ahead")
            

            if obj_label == "person":
                personCounter+=1
                if float(distances[ind]) < 72:
                    personCounter6feet+=1
            else:
                    objDic[obj_label][0]+=1
                    # first index is number of objects with the same labels, second index is if the object is detected in the front, 
                    # third index is if the object is detected in the left, fourth is if the obhject is detected in the right.
                    if detectedFront == True:
                        objDic[obj_label][1]+=1
                    if detectedLeft == True:
                        objDic[obj_label][2]+=1
                    if detectedRight == True:
                        objDic[obj_label][3]+=1
                    

        
        f = open("countPeople.txt", "w")
        f.write(str(personCounter))
        f.close()

        f = open("countPeople6Feet.txt", "w")
        f.write(str(personCounter6feet))
        f.close()

        f = open("detectObjs.txt", "w")
        f.write(str(dict(objDic)))
        f.close()

def default_factory():
    return [0, 0, 0, 0]


def cap_retrieve(cap):
    for i in range(4):
        isGrab = cap.grab()

    return cap.retrieve()



def main():
    # processing data
    print("main running")
    field_name = ["image_name", "image_id", "objectID", "class_number", "class_name", "y_min", "x_min", "y_max", "x_max",  "accuracy", "distance_pred"]
    # adding to dictionary
    with open('out.csv', 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = field_name)
        writer.writeheader()
    detect = det_model()

app = Flask(__name__)

def main_2():
    # Get webcam 
    cap = cv2.VideoCapture("http://192.168.1.182:8888/")
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
    print("camera started")
    # cap.set(cv2.CAP_PROP_FPS, 1)

    walker = smartWalker()
    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    count = 1
    while True:
        try:
            #capture frame
            print(count)
            count +=1
            ret, frame  = cap_retrieve(cap)
            if not ret:
                break
            # cap.release()
            # cap = cv2.VideoCapture("http://192.168.4.1:8081/video_feed")
            # cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
            frame, boxes, classes, scores, distances = walker.process_img(frame, visualize = False)
            
            # show frame by frame

            cv2.imshow('frame', frame)
            key = cv2.waitKey(10)
            #if key == 27: # exit on ESC
            #    break
            # boxes, classes, scores, distances = [[0,0,1,0],[0,0,1,0],[0,0,1,0],[0,0,1,0]], [1,1,1,1], [0,0,0,0], [0,0,0,0]
            give_directions(boxes, classes, scores, distances)

        except KeyboardInterrupt:
            print("Bye\n\n")
            cap.release()
            cv2.destroyAllWindows()
            break
    

class smartWalker:

    def __init__(self, distance_model_path='data.bin',
                 det_model_path = './efficientdet-d5'):
        # pdb.set_trace()
        
        self.det_sess = self.load_detection_session(det_model_path)
        self.dist_model = self.load_distance_model(distance_model_path)


    def load_detection_session(self, det_model_path):
        sess = tf.Session()
        tf.saved_model.load(sess, ['serve'], det_model_path)
        return sess 

    def load_distance_model(self, dist_model_path):
        model = None
        if os.path.isfile(dist_model_path):
            with open(dist_model_path, 'rb') as f:
                model = pickle.load(f)
        else:
            #todo train
            return model
        
        return model

    def process_img(self, img, visualize=False, min_score_thresh=0.6,
                    max_boxes_to_draw = 30, line_thickness=2, **kwargs):
        if isinstance(img, str):
            img = np.array(PIL.Image.open(img))
        else:
            img = np.array(img)

        params = inference.hparams_config.get_detection_config('efficientdet-d5').as_dict()
        label_map = params.get('label_map', None)
        
        detections = self.det_sess.run('detections:0', {'image_arrays:0': [img]})
        prediction = detections[0]
        boxes = prediction[:, 1:5]
        classes = prediction[:, 6].astype(int)
        scores = prediction[:, 5]

        label_map = label_util.get_label_map(label_map or 'coco')
        category_index = {k: {'id': k, 'name': label_map[k]} for k in label_map}

        distances = []
        for ind, [y_min, x_min, y_max, x_max] in enumerate(boxes):
            certainty = scores[ind]
            class_number = classes[ind]
            distances.append(self.dist_model.predict([[y_min, x_min, y_max , x_max, certainty, class_number]]))

        processed_img = vis_utils.visualize_boxes_and_labels_on_image_array(
                                img,
                                boxes,
                                classes,
                                scores,
                                category_index,
                                distances,
                                min_score_thresh=min_score_thresh,
                                max_boxes_to_draw=max_boxes_to_draw,
                                line_thickness=line_thickness,
                                **kwargs)
        if visualize:     
            img_plot = plt.imshow(processed_img)
            plt.show()

        boxes_filtered = []
        classes_filtered = []
        scores_filtered = []
        distances_filtered = []

        for i in range(len(scores)):
            if scores[i] > min_score_thresh:
                 boxes_filtered.append(boxes[i])
                 classes_filtered.append(classes[i])
                 scores_filtered.append(scores[i])
                 distances_filtered.append(distances[i])

        return processed_img, boxes_filtered, classes_filtered, scores_filtered, distances_filtered


@app.route('/', methods=['GET'])
def index():
    main_2()
    return 'Machine Learning Inference'

@app.route('/countPeople', methods=['GET'])
def index1():
    f = open("countPeople.txt", "r")
    theLabel = f.readline()
    print(theLabel)
    return jsonify(theLabel)

@app.route('/countPeople6Feet', methods=['GET'])
def index2():
    f = open("countPeople6Feet.txt", "r")
    theLabel = f.readline()
    print(theLabel)
    return jsonify(theLabel)

@app.route('/detectObjs', methods=['GET'])
def index3():
    f = open("detectObjs.txt", "r")
    theLabel = f.readline()
    print(theLabel)
    return jsonify(theLabel)

if __name__ == "__main__":
    print("main running")
    app.run(debug=True, host='0.0.0.0')
    
    #main()