import numpy
import scipy
import cv2
from scipy import ndimage
from skimage import feature

im = scipy.misc.imread('C:/Users/TD/Desktop/temporary/pics/12718221_952813414826074_6094924841739412499_n.jpg')
im = im.astype('int32')
dx = ndimage.sobel(im, 0)  # horizontal derivative
dy = ndimage.sobel(im, 1)  # vertical derivative
mag = numpy.hypot(dx, dy)  # magnitude
mag *= 255.0 / numpy.max(mag)  # normalize (Q&D)
scipy.misc.imsave('C:/Users/TD/Desktop/sobel.jpg', mag)