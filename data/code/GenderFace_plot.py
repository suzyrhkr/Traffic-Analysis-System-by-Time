import os, scipy.io
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, transform
import glob
from scipy import io
from tensorflow.keras import layers, applications, models, preprocessing, callbacks, optimizers, backend

# In[]
 # img 별로 수정
 WIDTH, HEIGHT = 121, 170

# In[]
def get_input(path):
  from skimage import io
  img = io.imread(path)

  return img

def preprocess_input(image):
  image = np.uint8(np.round(transform.resize(image, (HEIGHT, WIDTH), preserve_range=True)))
  image = preprocessing.image.img_to_array(image)
  image = np.expand_dims(image, axis=0)
  image = applications.vgg16.preprocess_input(image)

  return image

images = glob.glob('/Users/suzykwak/Desktop/gender_face/man/face_0.jpg')
images.sort()

# In[]
BATCH_SIZE=1

for num in range(1):
    # 순서대로 x 중심좌표, y 중심좌표, width 길이, height 길이 (0~1 사이로 normalization)
    annots_coord = [0.5, 0.5, 1, 1]

    # annots_x, annots_y: bounding box 중심 좌표
    annots_x = annots_coord[0] * WIDTH
    annots_y = annots_coord[1] * HEIGHT
    width = (annots_coord[2] * WIDTH) / 2
    height = (annots_coord[3]*HEIGHT) / 2

    x_min = annots_x - width
    x_max = annots_x + width
    y_min = annots_y - height
    y_max = annots_y + height

    # image plot
    img = plt.imread(images[num])
    fig, ax = plt.subplots()
    ax.imshow(img)

    ax.plot(annots_x, annots_y, '+', color='red')
    ax.plot(x_min, y_min, 'x', color='blue')
    ax.plot(x_max, y_max, 'x', color='blue')
    ax.plot()

    # 상황에 맞춰 수정
    plt.xlim(-10, WIDTH+10)
    plt.ylim(HEIGHT+10,-10)
    plt.show()
