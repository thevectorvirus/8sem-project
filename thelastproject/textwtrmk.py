#text watermark
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from PIL import ImageFont
from PIL import ImageDraw

#image opening
image=Image.open(r"image2.jpg")
image.show()
# plt.imshow(image)

#text watermarking
watermark_image=image.copy()
draw=ImageDraw.Draw(watermark_image)
font=ImageFont.truetype('arial.ttf',100)

#add watermark black color
draw.text((0,0), 'WTRMK', (0,0,0), font=font)
plt.subplot(1,2,1)
plt.title('Black Text')
watermark_image.show()
plt.imshow(watermark_image)

#add watermark white color
draw.text((0,0), 'WTRMK', (255,255,255), font=font)
plt.subplot(1,2,2)
plt.title('White Text')
watermark_image.show()
plt.imshow(watermark_image)