import sys
import os
from PIL import Image

# grab 1st and 2nd argument
source = sys.argv[1]
destination = sys.argv[2]
print(source, destination)
# # 1st arg: folder where JPG images are present
# # 2nd arg: folder where PNG images will be saved after conversion

# # if 2nd arg folder does not exist, create it
if not os.path.exists(destination):
    os.makedirs(destination)

# # loop through Pokedex folder
# print(f"./{source}{os.listdir(source)[0]}")
# path1 = f"./{source}{os.listdir(source)[0]}"
# img1 = Image.open(path1)
# path2 = f"./{destination}{os.listdir(source)[0][:-4]}.png"
# print(path2)
# img1.save(path2, 'png')
# print(img1)
# listPNG = []
for name in os.listdir(source):
    path1 = f"./{source}{name}"
    # print(path1)
    img = Image.open(path1)
    new_name = os.path.splitext(name)
    path2 = f"./{destination}{new_name[0]}.png"
    # path2 = f"./{destination}{name[:-4]}.png" # using list slicing, somehow ineffcient when file format is changed
    # print(path2)
    img.save(path2, 'png')
