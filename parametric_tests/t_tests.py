#%%
import scipy.stats as stats
import numpy as np


## One sample t
data=[13, 14, 13, 12, 14, 15, 16, 13, 14, 12]

x=stats.ttest_1samp(a=data, popmean=15)
print(x)

#%%

# Two sample t
group1=np.array([14, 12, 13, 12, 15, 12, 15, 15, 12, 13])
group2=np.array([12, 15, 14, 12, 13, 13, 14, 13, 12, 12])

# Test equal variances
vartest=stats.levene(group1, group2)
print(vartest)

# If variances are equal
varequal=stats.ttest_ind(a=group1, b=group2, equal_var=True)
print(varequal)

# If variances are not equal
varNOTequal=stats.ttest_ind(a=group1, b=group2, equal_var=False)
print(varNOTequal)

# Paired t test
pairedT=stats.ttest_rel(a=group1, b=group2)
print(pairedT)



