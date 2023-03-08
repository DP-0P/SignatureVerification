# '''IMPORTS'''
# from PIL import Image

# '''PRE-PROCESSING: RESIZING'''
# for person in range(1,11):
#   for attempt in range(1,6):
#     img_path = f"D:\cedar_minimal\\real\original_{person}_{attempt}.png"
#     print("-----------------------------")
#     print(img_path)
#     print("-----------------------------")
#     img = Image.open(img_path)
#     img = img.resize((500,500))
#     img = img.save(img_path)

"""
***TESTING IMAGE TILT CORRECTION AND DENOISER
"""
import cv2
image = cv2.imread("D:\cedar_minimal\\real\original_7_1.png")
height, width = image.shape[:2]
matrix = cv2.getRotationMatrix2D((width/2, height/2),-50,0.71)
translated = cv2.warpAffine(image, matrix, (width,height),borderMode=cv2.BORDER_CONSTANT,borderValue=(237, 237, 237))
cv2.imwrite("translated.png",translated)
denoise_img = cv2.fastNlMeansDenoisingColored(cv2.imread("translated.png"),None,2,3,7,21)
denoise_img = cv2.fastNlMeansDenoisingColored(cv2.imread("denoise.png"),None,2,7,9,21)
cv2.imwrite("denoise.png", denoise_img)
