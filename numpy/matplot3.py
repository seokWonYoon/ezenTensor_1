import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 0.5, 0.1  # mu 평균 / sigma 표준편차
s = np.random.normal(mu, sigma, 1000)

count, bins, ignored = plt.hist(s, 20, normed=True)

plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(- (bins - mu)
                                                       ** 2 / (2 * sigma**2)),       linewidth=3, color='y')
plt.show()