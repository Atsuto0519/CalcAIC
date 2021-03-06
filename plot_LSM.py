#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import LSM as LSM

#データ
data = np.loadtxt("lsmdata1_train.csv",delimiter=" ")

# データを表示
#print("data")
#print(data)

# データをわかりやすい配列に格納(pltに使いやすくしたいから)
data_x=[]
data_y=[]
for i in data :
    data_x.append(i[0])
    data_y.append(i[1])

# 次数Nを決定
#N = input("N == ")
N = 1

# LSMで誤差と重みベクトルcoeを計算
error, coe = LSM.LSM(data, int(N+1))
print("error:"+str(error))
print("coe:"+str(coe))

# データをプロット
plt.plot(data_x, data_y, "o")

# LSMで得た近似線をプロット
test_x = np.arange(min(data_x), max(data_x), 0.1)
plt.plot(test_x, LSM.quation_LSM(coe, test_x))
plt.show()
