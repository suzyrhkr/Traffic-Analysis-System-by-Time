# In[]
voc_file = open("/Users/suzykwak/Desktop/voc_name.txt", "r")
voc_list = []

for line in voc_file:
    stripped_line = line. strip()
    line_list = stripped_line. split('.')
    voc_list. append(line_list[0]+'.jpg')

voc_file. close()
print(voc_list)

# In[]

import cv2
import numpy as np
import logging
import os
import logging
import logging.config
from os import listdir
from os.path import isfile, join

class ImageCopy:
    def __init__(self, source_folder, destination_folder, file_name):
        self.logger = logging.getLogger('odir')
        self.source_folder = source_folder
        self.destination_folder = destination_folder
        self.file_name = file_name

    def copy_file(self):
        file = os.path.join(self.source_folder, self.file_name)
        image = cv2.imread(file)

        file_copy = os.path.join(self.destination_folder, self.file_name)
        cv2.imwrite(file_copy, image)

def process_all_images():
    files = [f for f in listdir(source_folder) if isfile(join(source_folder, f))]
    for file in files:
        if file in voc_list:
          print(file)
          # destination folder
          ImageCopy(source_folder, "/Users/suzykwak/Desktop/GenderDetection/PascalVOC/processed_voc", file).copy_file()

if __name__ == '__main__':
# source_folder
    source_folder = r'/Users/suzykwak/Desktop/GenderDetection/PascalVOC/voc_train+test'
    process_all_images()
