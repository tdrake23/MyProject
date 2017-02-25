from scipy import misc
import matplotlib.pyplot as plt

f = misc.face()
misc.imsave('face.png', f) # uses the Image module (PIL)
plt.imshow(f)
plt.show()