import numpy as np
from PIL import Image
from PIL import ImageOps
pil_img = Image.open('text_img.png')
pil_img = ImageOps.grayscale(pil_img)
# pil_img.show()
img = np.array(pil_img)
img = 255. - img
print(img.shape)
# img = ImageOps.grayscale(pil_img)
# tmp = Image.fromarray(img)
# tmp.show()
img_mean = np.mean(img)
print(img_mean)
img_sum = np.sum(img , axis=1)
# print(img_sum.shape)
j = 0
img_list = []
for i in range(1, img.shape[0]):
    if img_sum[i] == 0:
        img_list.append(img[j:i, :])
        j=i
img_list.append(img[j:, :])
    

def get_char(npimg, c):
    print(npimg.shape, 'line')
    line_sum = np.sum(npimg, axis=0)
    print('here we are')
    print(max(line_sum))
    j = 0
    char_list = []
    for i in range(1, npimg.shape[1]):
        if line_sum[i]==0: #(line_sum[i]/npimg.shape[0]) < img_mean:
            char_list.append(npimg[:, j:i])
            j = i
    char_list.append(npimg[:, j:])
    print(len(char_list), 'len of char list')
    cnt = 0
    for i in range(len(char_list)):
        if np.sum(char_list[i]) !=0:
            pil_char = Image.fromarray(char_list[i])
            pil_char = pil_char.convert('RGB')
            pil_char.save(str(c)+'_'+str(cnt)+'img.jpg')
            cnt +=1
c = 0
for i in range(len(img_list)):
    if np.sum(img_list[i]) != 0:
        # saving line
        pil_line = Image.fromarray(img_list[i])
        pil_line = pil_line.convert('RGB')
        pil_line.save(str(c)+'img.png')
        #going further for character
        line = pil_line.convert('1')
        line = np.array(line)
        get_char(line, c)

        c+=1
print(c)