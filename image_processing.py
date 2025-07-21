import cv2
from google.colab.patches import cv2_imshow
# from PIL import Image
# from IPython.display import display

# opening with cv2
img = cv2.imread("image.jpg")
# cv2_imshow(img)

# opening with PIL
# img = Image.open("image.jpg")
# display(img)

resized = cv2.resize(img, (300, 300))
# cv2_imshow(resized)

cropped = img[100:180, 50:480]
cv2_imshow(cropped)

flipped = cv2.flip(cropped, -1)
cv2_imshow(flipped)

rotated = cv2.rotate(cropped, cv2.ROTATE_90_CLOCKWISE)
cv2_imshow(rotated)

gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
cv2_imshow(gray)

cv2.imwrite("edited.png", cropped)




# Apply Gaussian Blur
gaussian = cv2.GaussianBlur(img, (5,5), 0)

# Apply Median Filtering
median = cv2.medianBlur(img, 5)

# Apply Bilateral Filtering
bilateral = cv2.bilateralFilter(img, 9, 75, 75)

# Show results
cv2.imshow("Original", img)
cv2.imshow("Gaussian Blur", gaussian)
cv2.imshow("Median Filtering", median)
cv2.imshow("Bilateral Filtering", bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()




# Load grayscale image
img = cv2.imread("document.jpg", cv2.IMREAD_GRAYSCALE)

# Apply simple thresholding
_, thresh_simple = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Apply adaptive thresholding
thresh_adaptive = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                        cv2.THRESH_BINARY, 11, 2)

# Apply Otsu’s Binarization
_, thresh_otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Show results
cv2.imshow("Simple Threshold", thresh_simple)
cv2.imshow("Adaptive Threshold", thresh_adaptive)
cv2.imshow("Otsu's Threshold", thresh_otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()




# Load grayscale image
img = cv2.imread("document.jpg", cv2.IMREAD_GRAYSCALE)

# Apply Histogram Equalization
hist_eq = cv2.equalizeHist(img)

# Apply CLAHE
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
clahe_img = clahe.apply(img)

# Show results
cv2.imshow("Original", img)
cv2.imshow("Histogram Equalization", hist_eq)
cv2.imshow("CLAHE", clahe_img)
cv2.waitKey(0)
cv2.destroyAllWindows()




# Load grayscale image
img = cv2.imread("document.jpg", cv2.IMREAD_GRAYSCALE)

# Apply Non-Local Means Denoising
denoised = cv2.fastNlMeansDenoising(img, None, 30, 7, 21)

# Show results
cv2.imshow("Original", img)
cv2.imshow("Denoised", denoised)
cv2.waitKey(0)
cv2.destroyAllWindows()
