from scipy import misc
import matplotlib.pyplot as plt

f = misc.face()


f = f[300:600,300:600]
misc.imsave('face.png', f) # uses the Image module (PIL)
plt.imshow(f)
plt.show()

#hello