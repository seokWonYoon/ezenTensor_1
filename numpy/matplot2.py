import numpy as np
import matplotlib.pyplot as plt

x= np.arange(0, 10)
y = x**2

plt.title("그래프")
plt.xlabel("시간")
plt.ylabel("거리")
# plt.plot(x, y, 'r') # 라인 색 red
# plt.plot(x, y, '<') # 라인타입 < > 꺾은선

plt.show()