import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 设置均值和标准差
mu = 0  # 均值
sigma = 1  # 标准差

# 生成x轴数据
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)

# 计算高斯分布的概率密度函数
y = norm.pdf(x, mu, sigma)

# 创建图形
plt.figure(figsize=(10, 6))

# 绘制高斯分布曲线
plt.plot(x, y, 'b-', linewidth=2, label=f'高斯分布 (μ={mu}, σ={sigma})')

# 填充曲线下方的区域
plt.fill_between(x, y, alpha=0.2)

# 添加标题和标签
plt.title('高斯分布曲线', fontsize=16)
plt.xlabel('x', fontsize=14)
plt.ylabel('概率密度', fontsize=14)

# 添加网格
plt.grid(True, linestyle='--', alpha=0.7)

# 添加图例
plt.legend(fontsize=12)

# 显示图形
plt.show()