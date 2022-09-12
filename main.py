import numpy as np
import matplotlib.pyplot as plt


def lerp(v0, v1, t):
    return (1 - t) * v0 + t * v1


size = 100
image = np.zeros((size, size, 3), dtype="uint8")
assert image.shape[0] == image.shape[1]

color1 = [255, 128, 0]
color2 = [0, 128, 255]

for i, v in enumerate(np.linspace(0, 1, image.shape[0])):
    r = lerp(color1[0], color2[0], v)
    g = lerp(color1[1], color2[1], v)
    b = lerp(color1[2], color2[2], v)
    image[i, :, :] = [r, g, b]

plt.figure(1)

rotate = np.zeros(image.shape)
rotate = rotate.astype(int)
for i in range(size):
    rotate[i, i] = image[:, 0][size-1-i]

for i in range(size):
    for j in range(size):
        rotate[i, j] = rotate[(i+j)//2, (i+j)//2]

plt.imshow(rotate)
plt.show()