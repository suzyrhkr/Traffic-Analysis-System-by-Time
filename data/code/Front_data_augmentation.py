# In[]
from PIL import Image
import glob

# In[]
img = Image.open('/Users/fjdks/Desktop/chaewon_docs/study/Capstone Design/Gender-Detection-master2/gender_dataset_face+labels/man/000001.jpg')
# img.show()
flipimg = img.transpose(Image.FLIP_LEFT_RIGHT)
# flipimg.show()

flipimg.save('/Users/fjdks/Desktop/chaewon_docs/study/Capstone Design/Gender-Detection-master2/gender_dataset_face+labels/man_flip/'+ace+'.jpg',format='JPEG')

# In[]
i=0
for infile in glob.glob('/Users/fjdks/Desktop/chaewon_docs/study/Capstone Design/Gender-Detection-master2/gender_dataset_face+labels/man/*.jpg'):
    with Image.open(infile) as im:
        flipimg=im.transpose(Image.FLIP_LEFT_RIGHT)

        flipimg.save('/Users/fjdks/Desktop/chaewon_docs/study/Capstone Design/Gender-Detection-master2/gender_dataset_face+labels/man_flip/'+str(i)+'.jpg',format='JPEG')
        i=i+1

# In[]

i=0
for infile in glob.glob('/Users/fjdks/Desktop/chaewon_docs/study/Capstone Design/Gender-Detection-master2/gender_dataset_face+labels/woman/*.jpg'):
    with Image.open(infile) as im:
        flipimg=im.transpose(Image.FLIP_LEFT_RIGHT)
        flipimg.save('/Users/fjdks/Desktop/chaewon_docs/study/Capstone Design/Gender-Detection-master2/gender_dataset_face+labels/woman_flip/'+str(i)+'.jpg',format='JPEG')
        i=i+1

print("Finish")

i=0
for infile in glob.glob('/Users/fjdks/Desktop/chaewon_docs/study/Capstone Design/Gender-Detection-master2/gender_dataset_face+labels/woman/*.jpg'):
    with Image.open(infile) as im:
        flipimg=im.transpose(Image.FLIP_LEFT_RIGHT)
        flipimg.save('/Users/fjdks/Desktop/chaewon_docs/study/Capstone Design/Gender-Detection-master2/gender_dataset_face+labels/woman_flip/'+str(i)+'.jpg',format='JPEG')
        i=i+1

print("Finish")
