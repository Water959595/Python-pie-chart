import matplotlib.pyplot as plt

item = ["trans","food","book","entertain"]
cost = [3000,8000,2000,3500]

div = 0.1           #分割大小
exp = (0, div, 0, div) #指定分割區域
plt.pie(cost, labels = item, explode = exp)  #圓餅圖 (數值,名稱,分割大小)
plt.show()
