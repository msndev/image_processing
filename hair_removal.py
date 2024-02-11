# -*- coding: utf-8 -*-
"""IP Proj.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1k1FtfRUpgkWzYjt3MNwgMRyx5PqMCLon

# Artifact Hair Removal
"""

from google.colab import drive
drive.mount('/content/drive',force_remount=True)

abs_test_path="/content/drive/MyDrive/Finalskinimages/melanoma"
import os

img_test = [img_file for img_file in os.listdir(abs_test_path) if os.path.isfile(os.path.join(abs_test_path, img_file)) and img_file.endswith('.jpg')]

print(img_test)

# Commented out IPython magic to ensure Python compatibility.
# % matplotlib inline
import skimage
print(skimage.__version__)
import numpy as np
from PIL import Image, ImageFont, ImageDraw
from PIL.ImageChops import add, subtract, multiply, difference, screen
import PIL.ImageStat as stat
from skimage.io import imread, imsave, imshow, show, imread_collection, imshow_collection
from skimage import color, viewer, exposure, img_as_float, data
from skimage.transform import SimilarityTransform, warp, swirl
from skimage.util import invert, random_noise, montage
import matplotlib.image as mpimg
import matplotlib.pylab as plt
from scipy.ndimage import affine_transform, zoom
from scipy import misc

"""**READING IMAGES FROM FOLDER**"""

import glob
images = glob.glob(abs_test_path + '/*.jpg')

images

for file in images:
 # print(file)
  im = Image.open(file) # read the image, provide the correct path
  print(im.width, im.height, im.mode, im.format, type(im))
  # 453 340 RGB PNG <class 'PIL.PngImagePlugin.PngImageFile'>
  im.show() # display the image

for file in images:
  im = mpimg.imread(file) # read the image from disk as a numpy ndarray
  print(im.shape, im.dtype, type(im)) # this image contains an α channel, hence num_channels= 4
  # (960, 1280, 4) float32 <class 'numpy.ndarray'>
  plt.figure(figsize=(10,10))
  plt.imshow(im) # display the image
  plt.axis('off')
  plt.show()

from google.colab.patches import cv2_imshow

import cv2
import numpy as np
from PIL import Image
def ArtifactRemoval(img,k):
    #cv2_imshow(img)
    #plt.imshow(im) # display the image
    grayScale = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) #Convert the original image to grayscale
    #cv2_imshow(grayScale)

    kernel = cv2.getStructuringElement(1,(17,17)) #Kernel for the morphological filtering

    blackhat = cv2.morphologyEx(grayScale, cv2.MORPH_BLACKHAT, kernel) #BlackHat filtering
    #cv2_imshow(blackhat)

    ret,thresh2 = cv2.threshold(blackhat,10,255,cv2.THRESH_BINARY) #Intensify the hair countours in preparation for the inpainting algorithm
    print( thresh2.shape )
    #cv2_imshow(thresh2)

    dst = cv2.inpaint(img,thresh2,1,cv2.INPAINT_TELEA) #Inpaint the original image depending on the mask
    #cv2_imshow(dst)
    #plt.imshow(dst) # display the image
    im_pil = Image.fromarray(dst)
    plt.figure(figsize=(10,10))
    plt.imshow(im_pil) # display the image
    plt.axis('off')
    plt.show()
    path="/content/drive/MyDrive/Finalskinimages/output_melanoma"
    im_pil.save(path+"/out"+str(k)+".jpg")

from google.colab.patches import cv2_imshow
import cv2
k=1
for file in images:
  ##im = cv2.imread(file) # read the image from disk as a numpy ndarray
  im=mpimg.imread(file)
  ArtifactRemoval(im,k)
  k=k+1



segment_path="/content/drive/MyDrive/Finalskinimages/melanoma"

img_test = [img_file for img_file in os.listdir(segment_path) if os.path.isfile(os.path.join(segment_path, img_file)) and img_file.endswith('.jpg')]

print(img_test)

import glob
images = glob.glob(segment_path + '/*.jpg')

# Commented out IPython magic to ensure Python compatibility.
from skimage.filters.rank import enhance_contrast
from skimage.morphology import binary_dilation, disk
# % matplotlib inline
from skimage.io import imread
from skimage.color import rgb2gray
import matplotlib.pylab as pylab
from skimage.morphology import binary_erosion, rectangle
from skimage import exposure
def plot_gray_image(ax, image, title):
    ax.imshow(image, cmap=pylab.cm.gray),
    ax.set_title(title), ax.axis('off')

k=1
for file in images:

  image = rgb2gray(imread(file))
  sigma = 0.05
  noisy_image = np.clip(image + sigma * np.random.standard_normal(image.shape), 0, 1)
  enhanced_image = enhance_contrast(noisy_image, disk(5))
  equalized_image = exposure.equalize_adapthist(noisy_image)

  fig, axes = pylab.subplots(1, 3, figsize=[18, 7], sharex='row',sharey='row')
  axes1, axes2, axes3 = axes.ravel()
  #plot_gray_image(axes1, noisy_image, 'Original')
  #plot_gray_image(axes2, enhanced_image, 'Local morphological contrast enhancement')
  #plot_gray_image(axes3, equalized_image, 'Adaptive Histogram equalization')
  path="/content/drive/MyDrive/Finalskinimages/enhanced_nonmelanoma"
  im_pil = Image.fromarray(enhanced_image)
  im_pil.save(path+"/out"+str(k)+".jpg")
  k=k+1



abs_test_path="/content/drive/MyDrive/Finalskinimages/non-melanoma"
import os

img_test = [img_file for img_file in os.listdir(abs_test_path) if os.path.isfile(os.path.join(abs_test_path, img_file)) and img_file.endswith('.jpg')]

import glob
images = glob.glob(abs_test_path + '/*.jpg')

from google.colab.patches import cv2_imshow

import cv2
import numpy as np
from PIL import Image
def ArtifactRemoval(img,k):
    #cv2_imshow(img)
    #plt.imshow(im) # display the image
    grayScale = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) #Convert the original image to grayscale
    #cv2_imshow(grayScale)

    kernel = cv2.getStructuringElement(1,(17,17)) #Kernel for the morphological filtering

    blackhat = cv2.morphologyEx(grayScale, cv2.MORPH_BLACKHAT, kernel) #BlackHat filtering
    #cv2_imshow(blackhat)

    ret,thresh2 = cv2.threshold(blackhat,10,255,cv2.THRESH_BINARY) #Intensify the hair countours in preparation for the inpainting algorithm
    print( thresh2.shape )
    #cv2_imshow(thresh2)

    dst = cv2.inpaint(img,thresh2,1,cv2.INPAINT_TELEA) #Inpaint the original image depending on the mask
    #cv2_imshow(dst)
    #plt.imshow(dst) # display the image
    im_pil = Image.fromarray(dst)
    plt.figure(figsize=(10,10))
    plt.imshow(im_pil) # display the image
    plt.axis('off')
    plt.show()
    path="/content/drive/MyDrive/Finalskinimages/output_nonmelanoma"
    im_pil.save(path+"/out"+str(k)+".jpg")

from google.colab.patches import cv2_imshow
import cv2
k=1
for file in images:
  ##im = cv2.imread(file) # read the image from disk as a numpy ndarray
  im=mpimg.imread(file)
  ArtifactRemoval(im,k)
  k=k+1