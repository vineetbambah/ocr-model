import cv2
from pathlib import Path
for file in Path('./images/inverted').iterdir():
    image = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    inverted_image = cv2.bitwise_not(image)
    _,binary_img = cv2.threshold(inverted_image, 128, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(binary_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    output_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(output_image, contours, -1, (0, 255, 0), 2)
    cv2.imshow('Contours', output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


