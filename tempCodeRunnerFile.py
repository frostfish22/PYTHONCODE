import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn import datasets
loaded_data = datasets.load_boston()
data_X=loaded_data.data
data_y=loaded_data.target
model = LinearRegression()
model.fit(data_X,data_y)
X,y=datasets.make_regression(n_samples=100,n_features=1,n_targets=1,noise=10)   #n_samples表示样本数目，n_features特征的数目  n_tragets  noise噪音
plt.scatter(X,y)
plt.show()