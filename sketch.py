import cv2

#Get the image location and image file name
img_location='C:/Users/Acer/PycharmProjects/hello.py/'
filename='model1.png'

#read in the image
img=cv2.imread(img_location+filename)


#Convert the image to gray scale
gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Invert the image
Inverted_gray_image=255 - gray_image

#Blur the image
blurred_img=cv2.GaussianBlur(Inverted_gray_image,(21,21),0)

#invert the blur image
inverted_blur_image=255-blurred_img

#Convert the image into the pencil sketch
pencil_sketch=cv2.divide(gray_image,inverted_blur_image,scale=256.0)

#showing the image
cv2.imshow('Original Image',img)
cv2.imshow('Pencil Sketch Image',pencil_sketch)
cv2.waitKey(0)