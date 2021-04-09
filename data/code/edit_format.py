#CelebA 데이터로 포맷 변경
# In[]
import numpy as np
import matplotlib.pyplot as plt
import glob
from tensorflow.keras import layers, applications, models, preprocessing, callbacks, optimizers, backend
from PIL import Image

# In[]
# file_path: 기존 labels가 있는 폴더
file_path = glob.glob('/Users/suzykwak/Desktop/renamed_celeb4000/celeb4000_labels/*.txt')
file_path.sort()
print(len(file_path))

# In[]
for name in file_path:

    f = open(name,'r')
    # des_path: 저장 경로
    des_path = '/Users/suzykwak/Desktop/renamed_celeb4000/new_format/' + name[:-4].split('/')[-1] + '.txt'

    des_f = open(des_path, 'w')

    lines = f.readlines()

    # 한 줄씩 읽어오기
    for line in lines:
        line = line.rstrip('\n')
        context= line.split(' ')

        label = context[0]
        x_center = float(context[1])
        y_center = float(context[2])
        w = float(context[3])
        h = float(context[4])

        half_w = w/2
        half_h = h/2

        # x_min, y_min, x_max, y_max
        x_min = x_center - half_w
        y_min = y_center - half_h
        x_max = x_center + half_w
        y_max = y_center + half_h

        # 마지막 line에서만 개행 문자 넣지 않기
        if(line != lines[-1].rstrip('\n')):
            context = str(x_min) + ',' + str(y_min) + ',' + str(x_max) + ',' + str(y_max) + ',' + label + '\n'
        else:
            context = str(x_min) + ',' + str(y_min) + ',' + str(x_max) + ',' + str(y_max) + ',' + label

        des_f.write(context)

    #파일 닫기
    f.close()
    des_f.close()
