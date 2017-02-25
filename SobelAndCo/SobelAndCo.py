from scipy import misc
import matplotlib.pyplot as plt

f = misc.face()


f = f[300:600,300:600]
misc.imsave('face.png', f) # uses the Image module (PIL)
plt.imshow(f)
plt.show()

<<<<<<< HEAD
#blabla
=======
#hello
>>>>>>> 803708f3f80dbab52e39bf64cad115801ec3f8b6
