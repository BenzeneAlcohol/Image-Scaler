import cv2

img=cv2.imread('D:\College\stest.jpg') #This is for reading the image, you need to specify the exact directory of the image else it will show an object error
print("Enter the number of times you want to upscale/downscale the image")
n = float(input())
scaleper = n #how much upscaling/downscaling is required
width = int(img.shape[1]*scaleper) #images are in the form of arrays, width and heigh at at 2 locations
height = int(img.shape[0]*scaleper)#we are scaling both equally to maintain the aspect ratio
dimension = (width,height)#new dimensions
resized = cv2.resize(img,dimension,interpolation=cv2.INTER_AREA)#resizing the image
cv2.imshow('output',resized)#outputting the resized image
cv2.imwrite('newpic.tif',resized)#writing the resized image
print(resized.shape)#Unspcaled size is displayed
cv2.waitKey(0) #adding a wait key, so that we can see the output instead of it fading away
cv2.destroyAllWindows()

