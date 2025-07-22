import cv2
from google.colab.patches import cv2_imshow

# load image
img = cv2.imread("noisy.jpg")
cv2_imshow(img)

# denoise with bilateral filter
bilateral = cv2.bilateralFilter(img, 9, 75, 75)
cv2_imshow(bilateral)

# convert to HSV color space
hsv = cv2.cvtColor(bilateral, cv2.COLOR_BGR2HSV)

# apply histogram equalization on v channel (brightness)
h, s, v = cv2.split(hsv)
v_eq = cv2.equalizeHist(v)

# merge and convert back to BGR
hsv_eq = cv2.merge([h, s, v_eq])
img_eq = cv2.cvtColor(hsv_eq, cv2.COLOR_HSV2BGR)
cv2_imshow(img_eq)

# denoise
denoised = cv2.fastNlMeansDenoising(img_eq, None, 20, 11, 51)
cv2_imshow(denoised)

cv2.imwrite("cleaned.jpg", denoised)
