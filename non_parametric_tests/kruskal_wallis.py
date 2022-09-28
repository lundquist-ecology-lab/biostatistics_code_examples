#%%
import pandas as pd

df = pd.read_csv("../example_data/iris.csv")

# Python does not  like the "." in column namesso switch to snake_case
df.columns = df.columns.str.replace(".","_", regex=False)

#%%
from scipy import stats

setosa = df.loc[df['Species'] == "setosa"]
versicolor = df.loc[df['Species'] == "versicolor"]
virginica = df.loc[df['Species'] == "virginica"]

stats.kruskal(setosa['Petal_Width'], versicolor['Petal_Width'], virginica['Petal_Width'])
