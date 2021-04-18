'''정규화가 안 된(annotations) 데이터를 각 이미지 크기에 맞추어 정규화하는 코드'''
# In[]
import glob,os
from PIL import Image

# In[]
image_path = glob.glob('/Users/suzykwak/Desktop/0417_voc+celeba/*.jpg')
image_path.sort()
txt_path = '/Users/suzykwak/Desktop/new_gt/'
des_path = '/Users/suzykwak/Desktop/destination/'

for name in image_path:

    img = Image.open(name)
    WIDTH, HEIGHT = img.size

    # name이름으로 txt파일 열기
    file = txt_path + name.split('.')[0].split('/')[-1] + '.txt'
    txt = open(file, 'r')

    des_full_path = des_path + name.split('.')[0].split('/')[-1] + '.txt'
    des_f = open(des_full_path, 'w')

    lines = txt.readlines()

    for line in lines:

        line = line.rstrip('\n')
        data = line.split(' ')

        label = data[0]
        x = float(data[1]) / WIDTH
        y = float(data[2]) / HEIGHT
        w = float(data[3]) / WIDTH
        h = float(data[4]) / HEIGHT

        if(line != lines[-1].rstrip('\n')):
            contents = label + ' ' + str(x) + ' ' + str(y) + ' ' + str(w) + ' ' + str(h) + '\n'
        else:
            contents = label + ' ' + str(x) + ' ' + str(y) + ' ' + str(w) + ' ' + str(h)

        print(contents)
        des_f.write(contents)

    des_f.close()
    txt.close()
