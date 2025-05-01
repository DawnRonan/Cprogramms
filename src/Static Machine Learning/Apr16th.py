import matplotlib.pyplot as plt
import numpy as np
#task one
# 三个点的坐标（可根据需要修改）
points = [(1, 2), (4, 3), (2, 5)]

# 拆分 x 和 y 坐标
x = [p[0] for p in points]
y = [p[1] for p in points]

# 是否闭合图形（三角形）
closed = True  # 设置为 False 只绘制折线

if closed:
    # 回到起点，形成闭合三角形
    x.append(points[0][0])
    y.append(points[0][1])

# 绘图
plt.figure(figsize=(6, 6))
plt.plot(x, y, marker='o', linestyle='-', color='blue', linewidth=2)
plt.grid(True)
plt.title("连接三点的图形")

# 标注每个点
for i, (xi, yi) in enumerate(points):
    plt.text(xi + 0.1, yi + 0.1, f"P{i+1}({xi},{yi})", fontsize=10)

plt.axis('equal')  # 保持坐标比例
plt.show()

#task two
a = np.array(1, 1.1, 1.2, 1.3, 1.4, 1.5)
avg = np.mean(data)
print(avg)  # 输出 3.0

#task three
n = 10
binary_str = bin(n)
print(binary_str)      # 输出 '0b1010'
print(binary_str[2:])  # 输出 '1010'（去掉 '0b' 前缀）git clone https://git.nexttechnologies.hu/education/ai.git

