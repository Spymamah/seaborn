from sklearn.datasets import load_iris
import pandas as pd

# Load the iris dataset
iris = load_iris()
print(type(iris))
print(iris)
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names,)
print(type(iris_df))
iris_df["truth"] = iris.target
print(iris_df.head())
# print("Dataset loaded successfully!")
# print("Features:", iris.feature_names)
# print("Target classes:", iris.target_names)
# print(iris.head()) 