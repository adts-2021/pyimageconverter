
from PIL import Image
import numpy
  
image = Image.open('images/adi_blue_128x160.png')
np_img = numpy.array(image)
  
# summarize some details about the image
# print(np_img.shape)
h,w,s = np_img.shape
builder = ""
builder = builder + ('{') #3
for y in range(h):
    builder = builder + ('{') #2
    for x in range(w):
        builder = builder + ('{') #1
        for z in np_img[y][x][0:3]:
            builder = builder + str(z) + ','
        builder = builder.strip(',')
        builder = builder + ('}') #1
        builder = builder + (',')
    builder = builder.strip(',')
    builder = builder + ('}') #2
    builder = builder + (',')
builder = builder.strip(',')
builder = builder + ('}') #3

print(builder)

