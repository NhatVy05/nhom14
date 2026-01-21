import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

M = 768
N = 1024

img = np.zeros((M, N), dtype=np.uint8)
cv.line(img, (0, 0), (N-1, M-1), 255)

# sử dụng cv vẽ 1 đường tròn có tâm trùng với tâm của ảnh, có bán kính là 100, màu trắng ,độ dày 2 pixel
cv.circle(img, (N//2, M//2), 300, 225, 2)


# plt.imshow(img, cmap='gray')
# plt.show()

# cv.imshow('image', img)
# if cv.waitKey(0) == ord('q'):
#     cv.destroyAllWindows()

# cv.line(img, (0, 0), (N-1, M-1), 255)

# m = 1024
# n = 768
# c = 3
# cl_img = np.zeros((m, n, 3), dtype=np.uint8)
# cl_img[100:300,:,0] = 255 # kênh màu xanh lá
# cl_img[250:500,:,1] = 255 # kênh màu đỏ
# cl_img[450:700,:,2] = 255 # kênh màu xanh dương

# cv.imshow('color image', cl_img)
# cv.waitKey(0)
# cv.destroyAllWindows()

#vẽ một bàn cờ vua đen trắng có kích thước 8x8, mỗi ô có kích thước 100x100 pixel
chessboard = np.zeros((800, 800), dtype=np.uint8)
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            cv.rectangle(chessboard, (j*100, i*100), ((j+1)*100, (i+1)*100), 255, -1)
cv.imshow('chessboard', chessboard)
cv.waitKey(0)
cv.destroyAllWindows()

#vẽ một bàn cờ vua đen đỏ có kích thước 8x8, mỗi ô có kích thước 100x100 pixel

