# Preston Malen
# March 2024
# Image compression via singular valued decomposition of pixel matrix
# Ref: https://www.youtube.com/watch?v=H7qMMudo3e8

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

A = imread('IMAGE.jpg')
X = np.mean(A, -1)

# original image in grayscale
img = plt.imshow(X)
img.set_cmap('gray')
og_size = os.stat('IMAGE.jpg').st_size
plt.axis('off')
plt.title('Grayscale Original Image')
plt.savefig('gray_pic.jpg')
plt.title('')
plt.show()


U, Sigma, Vtrans = np.linalg.svd(X, full_matrices=False) # effcient SVD
Sigma = np.diag(Sigma)

j = 0

# rank of matrix for approximation
rank = [5, 20, 250]

for r in rank:
    # reconstruction of the image matrix from the output of the SVD
    Xapprox = U[:,:r] @ Sigma[0:r,:r] @ Vtrans[:r,:]
    plt.figure(j+1)
    j += 1
    # this may just be Xapprox
    img = plt.imshow(Xapprox)
    img.set_cmap('gray')
    plt.axis('off')
    plt.title('rank = ' + str(r) + ' approximation')
    if r == max(rank):
        plt.title('')
        plt.savefig('comp_pic.jpg')
        plt.title('rank = ' + str(r) + ' approximation')
    plt.show()

cmp_size = os.stat('comp_pic.jpg').st_size
print('The original image size is ' + str(og_size/1000) + ' mb')
print('The compressed image size is ' + str(cmp_size/1000) + ' mb')

# this shows the "efficienty" of the SVD
# plt.figure(1)
# plt.semilogy(np.diag(Sigma))
# plt.title('Singular Values')

# plt.figure(2)
# plt.plot(np.cumsum(np.diag(Sigma))/np.sum(np.diag(Sigma)))
# plt.title('Cumulative Sum of Singular Values')
# plt.show()