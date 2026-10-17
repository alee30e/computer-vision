import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
#
img = cv.imread("butterfly.jpeg")
# cv.imshow("Fluture galben",img)
# cv.waitKey(0)
# cv.destroyAllWindows()
#
img = cv.imread("butterfly.jpeg",cv.IMREAD_GRAYSCALE)
# cv.imshow("Fluture gray",img)
# cv.waitKey(0)
# cv.destroyAllWindows()
#
H, W = img.shape
print(H,W)
#
img = cv.resize(img,(100, 100))
H, W = img.shape
print(H,W)
# cv.imshow("Fluture gray redimensionat",img)
# cv.waitKey(0)
# cv.destroyAllWindows()

# #a

v = img.flatten()
x = np.sort(v).reshape(10000, 1)
print(x)
# plt.plot(x)
# plt.show()

# a V2

x = np.sort(img, axis=None).reshape(10000, 1)
print(x)
# plt.plot(x)
# plt.show()

# #b

A = img[50:, 50:].copy()
# plt.imshow(A) # plt.imshow(A, cmap = "gray")
# plt.axis("off")
# plt.show()

# #c

t = np.median(x)
print(t)

# #d

B = img.copy()
B[B<t] = 0
B[B >= t] = 255

# plt.imshow(B, cmap = "gray")
# plt.axis("off")
# plt.show()

# #e

medie = img.mean()
print(medie)
#
C = img - medie
C[C < 0] = 0
C = np.uint8(C) # uint8 pt ca media poate fi cu vitgula iar pixelii au valori nat
#
# plt.imshow(C, cmap = "gray")
# plt.axis("off")
# plt.show()

# #f
mini = np.min(img)
print(mini)
l, c = np.where(img == mini)
print(l, c)

# 2

# a
import os
path = "colectiiImagini/set1/"
files = sorted(os.listdir(path))
print(files)

color_images =[]
gray_images = []

for image_name in files:
    if image_name.endswith("jpg"):
        img = cv.imread(path + image_name)
        color_images.append(img)
        img_gray = cv.imread(path + image_name, cv.IMREAD_GRAYSCALE)
        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        gray_images.append(img_gray)

color_images = np.array(color_images)
gray_images = np.array(gray_images)
print(color_images.shape)


img_medie_color = np.uint8(np.mean(color_images, axis = 0))
img_medie_gray = np.uint8(np.mean(gray_images, axis = 0))


# for image_name in files:
#     if image_name.endswith("jpg"):
#         img = cv.imread(path + image_name)
#         color_images.append(img)
#         img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#         gray_images.append(img_gray)

color_images = np.array(color_images)
gray_images = np.array(gray_images)

print(color_images.shape)
# 57 de imagini, dimensiuni de 215 pe 200 in 3 coloane

print(gray_images.shape)

mean_color_image = np.uint8(np.mean(color_images, axis = 0))
mean_gray_image = np.uint8(np.mean(gray_images, axis=0))

X = np.uint8(np.std(gray_images, axis = 0))

# plt.imshow(mean_color_image, cmap = "gray")
# plt.axis("off")
# plt.show()
#
# plt.imshow(mean_gray_image, cmap = "gray")
# plt.axis("off")
# plt.show()
#
# plt.imshow(X, cmap = "gray")
# plt.axis("off")
# plt.show()

img = cv.imread("butterfly.jpeg")
ws = 20
nw = 1000


img_crop = img[250:250+ws, 250:250+ws, :].copy()
H,W, _ = img.shape
print(H, W)
x = np.random.randint(0, W-ws+1, size = (nw))
y = np.random.randint(0, H-ws+1, size = (nw))

dist = np.zeros(nw)
for i in range(nw):
    patch = img[y[i]:y[i] + ws, x[i]:x[i] + ws, :]

    dif = img_crop.astype(float) - patch.astype(float)
    dist[i] = np.sqrt(np.sum(dif ** 2))

# val_minim = np.min(dist)
# indice = np.where( dist == val_minim)
indice = np.argmin(dist)

img_final = img.copy()
img_final[250:250+ws, 250:250+ws, :] = img[y[indice]:y[indice]+ws, x[indice]:x[indice] + ws, :]

plt.imshow(cv.cvtColor(img_final, cv.COLOR_BGR2RGB))
plt.axis("off")
plt.show()

