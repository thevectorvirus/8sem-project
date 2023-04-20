from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
#import imageio

def grayscale(rgb):
    return np.dot(rgb[...,:3], [0.199, 0.287, 0.214])
    
image=Image.open(r"image.png")
image.show()
plt.imshow(image)