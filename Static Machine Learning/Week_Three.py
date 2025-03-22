import numpy as np
import matplotlib.pyplot as plt
"""
# 定义 x 轴范围
x1 = np.linspace(0, 10, 100)   # 从 0 到 10 生成 100 个点
x2 = np.linspace(10, 25, 100)   # 从 10 到 25 生成 100 个点
x3 = np.linspace(25, 35, 100)  

# 定义对应的 y 值
y1 = x1
y2 = 10 * np.ones_like(x2)
y3 = x3 - 15

# 绘制分段函数
plt.plot(x1, y1, 'r', label=r"$y = x, 0 < x < 10$")
plt.plot(x2, y2, 'g', label=r"$y = 10, 10 < x < 25$")
plt.plot(x3, y3, 'b', label=r"$y = x - 15, x > 25$")

# 添加分段点
plt.scatter([0, 10], [0**2, 10], color='black', zorder=3)  # 连接点
plt.scatter([25], [10], color='black', zorder=3)  # 连接点

# 设置标题和标签
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Function")

# 显示网格和图例
plt.grid(True)
plt.legend()

# 显示图像
plt.show()
"""

def x_value(a, b):
    """
    返回两个数的和。
    
    :param a: 第一个数字
    :param b: 第二个数字
    :return: x的值
    """
    if a == 0:
        return "错误：除数a不能为零！"
    else:
        return -b / a

# 示例调用
result1 = x_value(2, -1)
result2 = x_value(4, -2)
result3 = x_value(0, 1)
print("结果是:", result1, result2, result3)

def create_identity_matrix(n):
    """
    创建一个 n x n 的单位矩阵，对角线元素为 1。
    
    :param n: 矩阵的大小
    :return: 对角线为 1 的 n x n 矩阵
    """
    return np.eye(n)

# 示例调用
matrix = create_identity_matrix(4)
print(matrix)

def triangle_area(a, b, c):
    """
    计算两个 3D 向量的叉积。
    
    :param a: 向量 a（列表或 NumPy 数组）
    :param b: 向量 b（列表或 NumPy 数组）
    :return: 叉积向量
    """
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    d = a - c
    e = b - c
    return abs(d[0] * e[1] - d[1] * e[0]) / 2

# 示例：计算两个 3D 向量的叉积

a = [1, 0]
b = [1, 4]
c = [0, 0]

area = triangle_area(a, b, c)   # 3D 向量的叉积
print(f"面积: {area}")

