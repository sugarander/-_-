import time
import math

iterations = 100000
x1, y1 = 1200000, 21200000
x2, y2 = 5003000, 6002130000

start_l2 = time.perf_counter()

for _ in range(iterations):
    _ = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

end_l2 = time.perf_counter()
time_l2 = end_l2 - start_l2 

start_l1 = time.perf_counter()

for _ in range(iterations):
    _ = abs(x2 - x1) + abs(y2 - y1)

end_l1 = time.perf_counter()
time_l1 = end_l1 - start_l1 


print(f"유클리드 거리 연산 시간 (변수 time_l2): {time_l2:.6f}초")
print(f"맨해튼 거리 연산 시간 (변수 time_l1): {time_l1:.6f}초")
print(f"맨해튼 거리가 약 {time_l2 / time_l1:.1f}배 빠름")