# '''IMPORTS'''
from PIL import Image
import cv2

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
image = cv2.imread("D:\cedar_minimal\\real\original_1_1.png")
denoise_img = cv2.fastNlMeansDenoisingColored(image,None,2,5,9,23)
cv2.imwrite("denoise.png", denoise_img)