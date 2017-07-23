import glob
import cv2

list = glob.glob("unresized/*.jpg")

for imagePath in list:
    image = cv2.imread(imagePath, 1)
    resized_image = cv2.resize(image, (int(image.shape[1]/2), int(image.shape[0]/2)) )
    imagePath = imagePath[9:-4]
    cv2.imwrite("resized/"+imagePath+"_resized.jpg", resized_image)
    #cv2.imwrite(imagePath+"_resized.jpg",)
