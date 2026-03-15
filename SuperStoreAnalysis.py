import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv(r"C:\Users\hario\Downloads\archive (2)\SuperStoreOrders.csv")
print(data.info())
print(data.head())
print(data.tail())


data["sales"] = pd.to_numeric(data["sales"].str.replace(",",""),errors="coerce")
data["sales"] = data["sales"].dropna()
sale = data["sales"]

profit = data["profit"]

avg_sale = np.mean(sale)
max_sale = np.max(sale)
min_sale = np.min(sale)

avg_profit = np.mean(profit)
max_profit = np.max(profit)
min_profit = np.min(profit)
print("The Average sale is :",avg_sale)
print("The Maximum Sale is :", max_sale)
print("The Minimum sale is :", min_sale)

print("The Average Profit is :",avg_profit)
print("The Maximum profit is :",max_profit)
print("The minimum profit is :",min_profit)

sns.barplot(x="year",y="profit",data=data)
plt.show()


