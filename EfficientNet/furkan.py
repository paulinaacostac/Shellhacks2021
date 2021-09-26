#print obj count, labels, bounding boxes and accuracy
import pdb
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
import inference
#from inference import ServingDriver
import numpy as np
#import tensorflow as tf
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

# if tf.executing_eagerly():
#    tf.compat.v1.disable_eager_execution()
import hparams_config
import PIL
from PIL import Image
from pathlib import Path



class Furkan:
    def __init__(self, boxes, classes, scores, labels):
        self.boxes = boxes
        self.classes = classes
        self.scores = scores
        self.labels = labels

    def for_Furkan(self):
      print("\n*******FURKANS CODE LOL **********")
      i = 0
      dict = {}
      #adding to dictionary
      while self.scores[i] > 0 and i < len(self.scores):
          if self.classes[i] not in dict:
            dict.update({self.labels.get(self.classes[i]): [(self.classes[i], self.boxes[i], self.scores[i])]})
          #appending if label already exist
          else:
            dict[self.labels.get(self.classes[i])].append([(self.classes[i], self.boxes[i],self.scores[i])])
          i += 1
      #print statements
      print("\ndict with stuff... -> "+ str(dict) + "\nObjection Detection Count: " + i)
      pdb.set_trace()
      return dict

class det_model:

    def __init__(self, model_file_name = 'efficientdet-d5'):
        print("det_model __init__ running")

        files = list(Path('./data_pics/DataSet1').rglob('*.jpg'))
        # imgs = []
        # files = [x for x in pic_folder]
        # for f in files:
        #     print(str(f))
        #     imgs.append(np.array(Image.open(f)))
        # print("imgs >>>" + str(imgs))

        # self.driver = inference.ServingDriver('efficientdet-d5', '/tmp//efficientdet-d5')
        # #driver = inference.ServingDriver('efficientdet-d0', '/tmp/efficientdet-d0')
        # self.driver.build()
        # self.driver.export('./efficientdet-d5')
        # pdb.set_trace()
        # self.run = self.driver.serve_images
        # predictions = self.driver.serve_images(imgs)
        # pdb.set_trace()
        # for i in range(len(imgs)):
        #     print("for loop: " + str(i))
        #     self.driver.visualize(imgs[i], predictions[i])
        #     self.driver.export('/Users/myatwin/REU/Project/ObjRec/automl/efficientdet/data_pics/processedPics')

        params = inference.hparams_config.get_detection_config('efficientdet-d5').as_dict()
        label_map = params.get('label_map', None)

        with tf.Session() as sess:
            tf.saved_model.load(sess, ['serve'], './efficientdet-d5')
            raw_images = []
            for f in tf.io.gfile.glob('./data_pics/DataSet1/*.jpg'):
                raw_images.append(np.array(PIL.Image.open(f)))
            # driver = inference.ServingDriver('efficientdet-d5', './efficientdet-d5', min_score_thresh=0.3)

            for ind, f in enumerate(files):
                # pdb.set_trace()
                detections = sess.run('detections:0', {'image_arrays:0': [raw_images[ind]]})
                img_name = os.path.basename(f)
                up_img = inference.visualize_image_prediction(raw_images[ind], detections[0], label_map=label_map, min_score_thresh=0.3)
                # driver.visualize(raw_images[ind], detections[0])
                PIL.Image.fromarray(up_img).save('./data_pics/processedPics/'+img_name)



        # self.driver = inference.ServingDriver('efficientdet-d5', './efficientdet-d5')
        # self.driver.build()
        # self.run = self.driver.serve_images
        # self.driver.visualize()
        # self.driver.export('/Users/myatwin/REU/Project/ObjRec/automl/efficientdet/data_pics/processedPics')
        # with tf.Session() as sess:
        #     tf.saved_model.load(sess, ['serve'], self.saved_model_dir)
        #     raw_images = []
        #     for f in tf.io.gfile.glob('/tmp/images/*.jpg'):
        #         raw_images.append(np.array(PIL.Image.open(f)))
        #     detections = sess.run('detections:0', {'image_arrays:0': raw_images})
        #     driver = inference.ServingDriver(
        #         'efficientdet-d0', '/tmp/efficientdet-d0')
        #     driver.visualize(raw_images[0], detections[0])
        #     PIL.Image.fromarray(raw_images[0]).save('/Users/myatwin/REU/Project/ObjRec/automl/efficientdet/data_pics/processedPics')


def main():
    detect = det_model()
    # while True:
    #     inp = input('Enter path to the image: ')
    #     img = np.array(Image.open(inp))
    #     pdb.set_trace()
    #     predictions = detect.run([img])
    #
    #     pdb.set_trace()

if __name__ == "__main__":
    # detect = det_model()

    main()