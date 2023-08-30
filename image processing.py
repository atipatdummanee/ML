
# โหลดภาพ
image_path = r"C:\Users\Admin\Desktop\images\captured_image_2024-05-18 11-15-57.jpg"

import cv2
import numpy as np
from matplotlib import pyplot as plt

# โหลดภาพ
image = cv2.imread(image_path)

# แปลงภาพเป็นสีเทา
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ปรับค่า Threshold
_, threshold_image = cv2.threshold(gray_image, 120, 255, cv2.THRESH_BINARY_INV)

# ตรวจสอบผลลัพธ์ของ Threshold Image
plt.imshow(threshold_image, cmap='gray')
plt.title('Threshold Image')
plt.show()

# ตรวจจับขอบเขตของพืช
contours, _ = cv2.findContours(threshold_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# วาดขอบเขตและวัดขนาด
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    size_text = f"Width: {w}px, Height: {h}px"
    cv2.putText(image, size_text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

# แสดงภาพที่มีการวัดขนาด
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Measured Plants')
plt.show()
print(f"Width: {w}px, Height: {h}px")