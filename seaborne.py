import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

tips = sns.load_dataset('tips')

print(tips.head())
# visualization of data
sns.relplot(data=tips, x = 'total_bill', y = 'tip', col = 'time', hue = 'smoker', style = 'smoker', size = 'size')
plt.show()
# i think hue 
# import seaborn as sns
# import matplotlib.pyplot as plt

# sns.set(style="darkgrid")
# tips = sns.load_dataset("tips")
# sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time")
# plt.show()

