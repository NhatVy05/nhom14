import cv2
import numpy as np
import math
from datetime import datetime

# Kích thước đồng hồ
WIDTH, HEIGHT = 800, 800
CENTER = (WIDTH // 2, HEIGHT // 2)
RADIUS = 350

# Màu sắc
CLOCK_FACE = (220, 220, 220)   # Mặt đồng hồ
HAND_COLORS = {
    'hour': (255, 0, 0),       # Xanh dương
    'minute': (0, 255, 0),     # Xanh lá
    'second': (0, 0, 255)      # Đỏ
}

def draw_roman_clock(frame):
    cv2.circle(frame, CENTER, RADIUS, CLOCK_FACE, -1)
    cv2.circle(frame, CENTER, RADIUS, (0, 0, 0), 8)

    # Vẽ vạch phút (60 vạch)
    for i in range(60):
        angle = math.radians(i * 6 - 90)
        length = 20 if i % 5 == 0 else 10
        x1 = int(CENTER[0] + (RADIUS - 20) * math.cos(angle))
        y1 = int(CENTER[1] + (RADIUS - 20) * math.sin(angle))
        x2 = int(CENTER[0] + (RADIUS - length) * math.cos(angle))
        y2 = int(CENTER[1] + (RADIUS - length) * math.sin(angle))
        cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 0), 2 if i % 5 == 0 else 1)

    # Chỉ vẽ 4 số: 3, 6, 9, 12 (vị trí 3h, 6h, 9h, 12h)
    roman_positions = [
        (12, 0),   # XII - 12 giờ (trên cùng)
        (3, 90),   # III  - 3 giờ (phải)
        (6, 180),  # VI   - 6 giờ (dưới)
        (9, 270)   # IX   - 9 giờ (trái)
    ]

    for num, angle_deg in roman_positions:
        angle = math.radians(angle_deg - 90)
        x = int(CENTER[0] + (RADIUS - 60) * math.cos(angle))
        y = int(CENTER[1] + (RADIUS - 60) * math.sin(angle))
        
        # Màu sắc khác nhau cho từng số
        color = (255, 255, 255) if num == 12 else (255, 200, 200) if num == 3 else \
                (200, 255, 200) if num == 6 else (200, 200, 255)
        
        cv2.putText(frame, str(num), (x - 20, y + 20),
                    cv2.FONT_HERSHEY_TRIPLEX, 1.8, color, 5, cv2.LINE_AA)

    return frame

def draw_hands(frame, hour, minute, second):
    # Kim giây (đỏ)
    sec_angle = second * 6 - 90
    sec_rad = math.radians(sec_angle)
    sec_x = int(CENTER[0] + (RADIUS - 40) * math.cos(sec_rad))
    sec_y = int(CENTER[1] + (RADIUS - 40) * math.sin(sec_rad))
    cv2.line(frame, CENTER, (sec_x, sec_y), HAND_COLORS['second'], 3)

    # Kim phút (xanh lá)
    min_angle = (minute + second / 60) * 6 - 90
    min_rad = math.radians(min_angle)
    min_x = int(CENTER[0] + (RADIUS - 80) * math.cos(min_rad))
    min_y = int(CENTER[1] + (RADIUS - 80) * math.sin(min_rad))
    cv2.line(frame, CENTER, (min_x, min_y), HAND_COLORS['minute'], 6)

    # Kim giờ (xanh dương)
    hour_angle = (hour % 12 + minute / 60) * 30 - 90
    hour_rad = math.radians(hour_angle)
    hour_x = int(CENTER[0] + (RADIUS - 140) * math.cos(hour_rad))
    hour_y = int(CENTER[1] + (RADIUS - 140) * math.sin(hour_rad))
    cv2.line(frame, CENTER, (hour_x, hour_y), HAND_COLORS['hour'], 10)

    cv2.circle(frame, CENTER, 15, (50, 50, 50), -1)  # Núm giữa

while True:
    frame = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
    frame = draw_roman_clock(frame)

    now = datetime.now()
    draw_hands(frame, now.hour, now.minute, now.second)

    cv2.imshow("Đồng hồ La Mã - Chỉ 4 số", frame)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()