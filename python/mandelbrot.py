import matplotlib.pyplot as plt
import numpy as np

# Z(n) = (Z(n-1))^2 + c
# Z(0) = c

def mandelbrot(c:complex, thresh:int=4, max_steps:int=25) -> int:
    '''
        Finds if a complex number diverges under max_steps and if it does then when.
    '''
    z=c
    i=1
    while i<max_steps and (z*z.conjugate()).real<thresh:
        z=z*z +c
        i+=1
    return i

def plotter(n, thresh, max_steps=25):
    # we use a complex plane
    ax = 2.48 / (n-1) # real axis
    ay = 2.26 / (n-1) # imaginary axis
    mapper = lambda x,y: (ax*x - 2, ay*y - 1.13)
    img=np.full((n,n), 255)
    # we use an incremental algorithm with a limit
    for x in range(n):
        for y in range(n):
            it = mandelbrot(complex(*mapper(x,y)), thresh=thresh, max_steps=max_steps)
            img[y][x] = 255 - it
    return img

n=1000 # iterations
img = plotter(n, thresh=4, max_steps=50)
plt.imshow(img, cmap="twilight")
plt.axis("off")
plt.show()