import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn

iris=pd.read_csv("../input/Iris.csv")
# iris.plot(kind="scatter", x="SepalLengthCm", y="SepalWidthCm")
iris.head()
print(iris.isnull().sum())

pd.concat([],abs())