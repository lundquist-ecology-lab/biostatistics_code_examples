#%%
import pandas as pd

# load data file

# Y needs to be continuous and needs to be organized into > two X groups.

df = pd.read_csv("../example_data/iris.csv")

# Python does not  like the "." in column namesso switch to snake_case
df.columns = df.columns.str.replace(".","_", regex=False)

#%%
import matplotlib.pyplot as plt
import seaborn as sns

# Boxplots and stipplots

ax = sns.boxplot(x='Species', y='Petal_Width', data=df, color="#99c2a2")
ax = sns.stripplot(x='Species', y='Petal_Width', data=df, color="#7d0013")
plt.show()


# %%
import scipy.stats as stats

## Interested in petal width

setosa = df.loc[df['Species'] == "setosa"]
versicolor = df.loc[df['Species'] == "versicolor"]
virginica = df.loc[df['Species'] == "virginica"]


# For just F and P value
fvalue, pvalue = stats.f_oneway(setosa['Petal_Width'], versicolor['Petal_Width'], virginica['Petal_Width'])
print(fvalue, pvalue)

# %%
## ANOVA table

import statsmodels.api as sm
from statsmodels.formula.api import ols


# Ordinary Least Squares model
model = ols('Petal_Width ~ Species', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
anova_table

# %%
# Tukey HSD
from bioinfokit.analys import stat

res = stat()
res.tukey_hsd(df=df, res_var='Petal_Width', xfac_var='Species', anova_model='Petal_Width ~ C(Species)')
res.tukey_summary


# %%
# Check assumptions
# QQ-plot
import statsmodels.api as sm
import matplotlib.pyplot as plt

sm.qqplot(res.anova_std_residuals, line='45')
plt.xlabel("Theoretical Quantiles")
plt.ylabel("Standardized Residuals")
plt.show()

# histogram
plt.hist(res.anova_model_out.resid, bins='auto', histtype='bar', ec='k') 
plt.xlabel("Residuals")
plt.ylabel('Frequency')
plt.show()

# %%
# Shapiro-Wilk test for normality
import scipy.stats as stats
w, pvalue = stats.shapiro(model.resid)
print(w, pvalue)

# %%
# Bartlett test for homogeneity of variances
import scipy.stats as stats
w, pvalue = stats.bartlett(setosa['Petal_Width'], versicolor['Petal_Width'], virginica['Petal_Width'])
print(w, pvalue)

# %%
## Levene's test for homogeneity of variances
from bioinfokit.analys import stat 
res = stat()
res.levene(df=df, res_var='Petal_Width', xfac_var='Species')
res.levene_summary

# It seems that we should be using the non-parametric ANOVA (Kruskal-Wallace)