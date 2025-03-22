import numpy as np

class SoftMarginPerceptron:
    def __init__(self, learning_rate=0.01, C=1.0, max_iter=1000):
        self.lr = learning_rate  # 学习率
        self.C = C  # 正则化参数
        self.max_iter = max_iter  # 迭代次数
        self.w = None  # 权重
        self.b = None  # 偏置

    def fit(self, X, y):
        """训练软间隔感知机"""
        n_samples, n_features = X.shape
        self.w = np.zeros(n_features)  # 初始化权重
        self.b = 0  # 初始化偏置
        self.xi = np.zeros(n_samples)  # 初始化松弛变量 ξ

        for _ in range(self.max_iter):
            for i, x_i in enumerate(X):
                # 计算 ξ_i
                self.xi[i] = max(0, 1 - y[i] * (np.dot(self.w, x_i) + self.b))

                # 误分类更新
                if self.xi[i] > 0:
                    self.w += self.lr * (y[i] * x_i - 2 * self.C * self.w)  # 更新权重
                    self.b += self.lr * y[i]  # 更新偏置

    def predict(self, X):
        return np.sign(np.dot(X, self.w) + self.b)

# 创建数据集
X = np.array([[2,3], [1,1], [3,1], [5,3], [4,2], [6,4]])
y = np.array([1, -1, -1, 1, 1, 1])

# 训练感知机
perceptron = SoftMarginPerceptron(learning_rate=0.1, C=0.1, max_iter=100)
perceptron.fit(X, y)

# 预测新样本
X_test = np.array([[3, 2], [2, 1]])
predictions = perceptron.predict(X_test)
print("Predictions:", predictions)
