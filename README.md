# SVD Image Compressor
A simple application of SVD to convert and compress images from RGB to grayscale.

Change the string `IMAGE.jpg` to the name of the image to be converted (must live in the same directory).

The image will be converted to grayscale and displayed. From there, each rank approximation will be displayed and the highest rank approximation will be saved as `comp_pic.jpg` .The comparison of the size of the two images will be printed.

The last two code blocks plot the singular values as well as the rolling sum of singular values to show the accuracy of the approximation.

Note: You may suppress all plotting except for `plt.savefig()` and still get the proper readout. 

I have also supplied a simple test image.

The formatting when saving the image is by no means optimal, but the idea here is to show how SVD can drastically reduce the size of an image while maintaining a majority of it's information.