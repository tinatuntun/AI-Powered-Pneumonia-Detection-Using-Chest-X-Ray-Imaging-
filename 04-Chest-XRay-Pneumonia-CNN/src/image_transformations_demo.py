import imageio.v2 as imageio
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi 

im=imageio.imread("brainpractice.jpg",mode = 'F')

#Translations

h, w = im.shape
com = ndi.center_of_mass(im)
# Calculate amount of shift needed
d0 = (h/2) - com[0]
d1 = (w/2) - com[1]

# Translate the brain towards the center
xfm = ndi.shift(im, shift=(d0, d1))

# Plot the original and adjusted images
fig, axes = plt.subplots(1,2)
axes[0].imshow(im, cmap='gray')
axes[1].imshow(xfm,cmap='gray')
axes[0].axis('off')
axes[1].axis('off')
plt.show()

#######################
#Rotations

# Rotate the shifted image
xfmR = ndi.rotate(xfm, angle=20, reshape=False)

# Plot the original and rotated images
fig, axes = plt.subplots(1,2)
axes[0].imshow(xfm, cmap='gray')
axes[1].imshow(xfmR,cmap='gray')
axes[0].axis('off')
axes[1].axis('off')
plt.show()

#######################
#Translate and Rescale

mat = [[0.9, 0,50]
       ,[0, 0.9,-100]
       ,[0, 0, 1]]
trans = ndi.affine_transform(im,mat)
fig, axes = plt.subplots(1,2)
axes[0].imshow(im, cmap='gray')
axes[1].imshow(trans,cmap='gray')
axes[0].axis('off')
axes[1].axis('off')
plt.show()
#Resampling

# Resample image
im_dn = ndi.zoom(xfmR, zoom=0.1)
im_up = ndi.zoom(xfmR, zoom=6)
print(im.shape)
print(im_dn.shape)
print(im_up.shape)

fig, axes = plt.subplots(1,3,figsize=(12,12))
axes[0].imshow(xfmR, cmap='gray')
axes[1].imshow(im_dn,cmap='gray')
axes[2].imshow(im_up,cmap='gray')
axes[0].axis('off')
axes[1].axis('off')
axes[2].axis('off')
plt.show()

#Interpolation

imInter=imageio.imread("inter.jpg",mode = 'F')
up0 = ndi.zoom(imInter, zoom=10, order=0)
up5 = ndi.zoom(imInter, zoom=10, order=4)

# Print original and new shape
print('Original shape:', imInter.shape)
print('Upsampled shape:', up0.shape)

fig, axes = plt.subplots(1,3,figsize=(12,12))
axes[0].imshow(imInter, cmap='gray')
axes[1].imshow(up0[500:1000,500:1000],cmap='gray')
axes[2].imshow(up5[500:1000,500:1000],cmap='gray')
axes[0].axis('off')
axes[1].axis('off')
axes[2].axis('off')
plt.show()
