''' 0,1 labels 와 2,3 labels 좌표 concatenating code'''
# In[]
import glob,os
from PIL import Image

# In[]
ex_path = glob.glob('/Users/suzykwak/Desktop/labels/*.txt')
ex_path.sort()
#print(len(ex_path))

new_path = glob.glob('/Users/suzykwak/Desktop/destination/*.txt')
new_path.sort()
#print(len(new_path))

#두 개 경로 pair 맞는지 확인
#print(ex_path[-1], new_path[-1])

#concat된 text files 저장할 경로
des_path = '/Users/suzykwak/Desktop/concatenate/'

# In[]

for i in range(len(ex_path)):

    ex_txt = open(ex_path[i], 'r')
    new_txt = open(new_path[i], 'r')

    # concat된 각 text file 저장 경로
    path = des_path + ex_path[i].split('.')[0].split('/')[-1] + '.txt'
    des_f = open(path, 'w')

    ex_lines = ex_txt.readlines()
    new_lines = new_txt.readlines()

    # ex_txt 파일 쓰기
    for line in ex_lines:
        data = line.rstrip('\n')

        # 마지막 줄이 아니면 개행 문자 넣기
        if(data != ex_lines[-1].rstrip('\n')):
            contents = data + '\n'
            des_f.write(contents)

        # 마지막 줄인 경우 new_txt 파일이 비었는지 확인
        else:
            # new_lines 비었을 경우 개행 문자 넣지 않기
            if not new_lines:
                des_f.write(data)

            #비어있지 않은 경우 개행 문자 넣기
            else:
                contents = data + '\n'
                des_f.write(contents)

    # new_txt 데이터 쓰기
    for line in new_lines:
        data = line.rstrip('\n')
        # 마지막 줄이 아닌 경우 개행 문자 넣기
        if(data != new_lines[-1].rstrip('\n')):
            contents = data + '\n'
            des_f.write(contents)
        # 마지막 줄인 경우 개행 문자 넣지 않기
        else:
            des_f.write(data)

    ex_txt.close()
    new_txt.close()
    des_f.close()
