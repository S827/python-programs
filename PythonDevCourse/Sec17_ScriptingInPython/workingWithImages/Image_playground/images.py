from PIL import Image

import os

filepath = './Pokedex/pikachu.jpg'
if os.path.exists(filepath):
    print('yes')
else:
    print('no')
img = Image.open(r'.\Pokedex\pikachu.jpg')
print(img)  # returns PIL image object

# print(img.format)  # return format of image
# print(img.size)  # returns size of image
# print(img.mode)  # returns mode of image which is RGB
# print(img.getpixel)
# print(img.putpixel)
# print(img.convert)
# print(img.width)

# # what functions and methods img has
# print(dir(img))  # returns list of func, methods, attributes Image supports

# filtered_img = img.filter(ImageFilter.BLUR)  # blur the image
# filtered_img.save('blur.png', 'png')  # saves the blurred image in png format

# smooth_img = filtered_img.filter(ImageFilter.SMOOTH)
# smooth_img.save('smoothPikachu.png', 'png')

# sharp_img = img.filter(ImageFilter.SHARPEN)
# sharp_img.save('sharp-pikachu.png', 'png')

# grey_img = img.convert('L')  # converts image to grey color, greyscale
# grey_img.save('grey-img.png', 'png')
# # grey_img.show()  # display the image
# rot_grey_img = grey_img.rotate(45)
# rot_grey_img.save('rot-grey.png', 'png')
# # rot_grey_img.show()
# grey_resized = grey_img.resize((300, 300))  # resize accepts tuple argument
# grey_resized.save('grey-resize.png', 'png')
# # grey_resized.show()

# box = (50, 50, 200, 200)
# crop_img = sharp_img.crop(box)
# crop_img.save('crop_img.png', 'png')
# # crop_img.show()

# img1 = Image.open('./astro.jpg')
# print(img1.size)
# new_img1 = img1.resize((400, 200))  # resize lose the aspect ratio
# new_img1.save('astro-resized.png', 'png')
# img1.thumbnail((400, 200))
# img1.save('astr-thumbnail.jpg')
# print(img1.size)
# img2 = Image.open('./astro.jpg')
# img2.thumbnail((400, 400))
# img2.save('astro-reresized.jpg')
# print(img2.size)
