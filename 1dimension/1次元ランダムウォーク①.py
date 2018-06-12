import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)  #乱数の初期化（同じランダムを繰り返す）
w = np.random.rand(1000) #1000個の乱数生成
w = np.where(w>0.5, 1, -1)#0.5以上は1,未満は-1
w = w.cumsum()  #累積和

print(w.min())
print(w.max())

print(w.argmin())#最初に-11になったインデックス
print(w.argmax())#最初に-35になったインデックス

plt.plot(np.arange(1000), w)
#plt.scatter(w.argmin(),w.min(),marker="D", c="r")
#plt.scatter(w.argmax(),w.max(),marker="D", c="r")
#plt.text(w.argmin(), w.min(), "min", fontsize=16)
#plt.text(w.argmax(), w.max(), "max", fontsize=16)
plt.show()
