import random
import numpy as np
import matplotlib.pyplot as plt

numbers = [random.randint(0, 100) for _ in range(100)]
sum = 0
for i in range(100):
    sum += numbers[i]  # Or any other value you want
average = sum / 100
print("The average is:", average)

x = np.linspace(-10, 10, 400)
x = x[x != 0]  # 排除 x = 0
y = 3 / x + x ** 2 + 2
plt.plot(x, y, 'r', label=r"$3 / x + x ** 2 + 2, -10 < x < 10 ^ x != 0$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Function")

# 显示网格和图例
plt.grid(True)
plt.legend()

# 显示图像
plt.show()

sentence = "I am learning"
word = "Python"

# 在句子后添加单词
new_sentence = sentence + " " + word
print(new_sentence)

