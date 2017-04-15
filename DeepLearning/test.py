import cv2
import os
from subprocess import call


call("python ./util/align-dlib.py ./images/training-images/extra align outerEyesAndNose ./aligned-images/ --size 96", shell=True)

# import time
#
# start = time.time()
# call("/home/nishikanto/torch/install/bin/lua ./batch-represent/main.lua -outDir ./generated-embeddings/ -data ./aligned-images/", shell=True)
# print("Embeddings generation time = {}".format(time.time() - start))
# call("python ./demos/classifier.py train ./generated-embeddings/", shell=True)
   #call("python ./demos/classifier.py infer ./generated-embeddings/classifier.pkl 0.jpg", shell=True)


