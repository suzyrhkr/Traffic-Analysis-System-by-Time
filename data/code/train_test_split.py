# 하나의 폴더에서 8:2로 나눠서 파일 이동

from glob import glob
import shutil
from sklearn.model_selection import train_test_split
# do test train splitting
# find image names
image_files = glob("Dataset(Celeb,Pascal)/data/*.jpg")
# remove file extension
image_names = [name.replace(".jpg","") for name in image_files]
# Use scikit learn function for convenience
train_names, test_names = train_test_split(image_names, random_state=35, test_size=0.2)

# 갯수 확인
print("total:",len(image_files))
print("train:",len(train_names))
print("test:",len(test_names))

# 파일 옮기기
# train
for file in train_names:
      image = file+'.jpg'
      txt = file+'.txt'

      shutil.move(image,'Dataset(Celeb,Pascal)/train/images')
      shutil.move(txt,'Dataset(Celeb,Pascal)/train/labels')

#test
for file in test_names:
    image = file + '.jpg'
    txt = file + '.txt'

    shutil.move(image, 'Dataset(Celeb,Pascal)/test/images')
    shutil.move(txt, 'Dataset(Celeb,Pascal)/test/labels')


