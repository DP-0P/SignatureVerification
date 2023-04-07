import cv2
img_size = 250
img = cv2.imread("D://cedar_original//full_org/original_9_9.png")
img = cv2.resize(img,(img_size, img_size), interpolation = cv2.INTER_AREA)
denoise_img_0 = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
denoise_img_1 = cv2.fastNlMeansDenoisingColored(img,None,2,5,9,23)
cv2.imshow("0",denoise_img_0)
cv2.imshow("1",denoise_img_1)
cv2.waitKey(0)