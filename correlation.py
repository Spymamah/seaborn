import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.datasets import load_diabetes

house = load_diabetes()

house_df = pd.DataFrame(house.data, columns=house.feature_names)

house_df['Price']= house.target
print(house_df.head())
correlation = house_df.corr()
plt.figure(figsize=(10,10))
sns.heatmap(correlation, cbar=True, square=True, fmt='.1f', annot=True, annot_kws={'size':8}, cmap='Blues')
plt.show()

