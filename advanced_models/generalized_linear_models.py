#%%

import pandas as pd

# Need some data
species_df = pd.read_csv("../example_data/forest_butterflies/butterfly_species.csv", sep = ';')
sites_df = pd.read_csv("../example_data/forest_butterflies/butterfly_sites.csv", sep = ';')

#%%
# We need to do some data managment, species and sites are grouped by "sites_ID"
sites_ID = sites_df['sites_ID'].values.tolist()

richness = []

for index, sites in enumerate(sites_ID):
    df = species_df.loc[species_df['sites_ID'] == sites]
    list1 = df['Species'].values.tolist()
    richness.insert(index, len(list1))    

#%%
import patsy
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.genmod.families import Poisson

# Here we can think of y and x, 
# or endogenous and exogenous, 
# or dependent and independent

data = {'Richness': richness,
        'A_mean_temp': sites_df['A_mean_temp'],
        'A_rainfall': sites_df['A_rainfall'],
        'Olsoneconame': sites_df['Olsoneconame'],
        'Ribeirovegtype': sites_df['Ribeirovegtype'],
        'BSRs': sites_df['BSRs']
}
analysis_df = pd.DataFrame(data)


## analysis_df['Richness'] = richness
#%%

fam = Poisson()
f0 = 'Richness ~  A_mean_temp + A_rainfall + C(Olsoneconame) + C(Ribeirovegtype) + C(BSRs)'
y, X = patsy.dmatrices(f0, data, return_type='matrix')

model_0 = sm.GLM(y, X, family=fam).fit()
print(model_0.summary())


from scipy import stats

def calculate_nested_f_statistic(small_model, big_model):
    """Given two fitted GLMs, the larger of which contains the parameter space of the smaller, return the F Stat and P value corresponding to the larger model adding explanatory power"""
    addtl_params = big_model.df_model - small_model.df_model
    f_stat = (small_model.deviance - big_model.deviance) / (addtl_params * big_model.scale)
    df_numerator = addtl_params
    # use fitted values to obtain n_obs from model object:
    df_denom = (big_model.fittedvalues.shape[0] - big_model.df_model)
    p_value = stats.f.sf(f_stat, df_numerator, df_denom)
    return (f_stat, p_value)

f1 = 'Richness ~  A_mean_temp + A_rainfall + C(Olsoneconame) + C(Ribeirovegtype)'
y, X = patsy.dmatrices(f1, data, return_type='matrix')

model_1 = sm.GLM(y, X, family=fam).fit()
calculate_nested_f_statistic(model_1, model_0)

f2 = 'Richness ~  A_mean_temp + A_rainfall + C(Olsoneconame)'
y, X = patsy.dmatrices(f1, data, return_type='matrix')

model_2 = sm.GLM(y, X, family=fam).fit()
calculate_nested_f_statistic(model_2, model_1)

f3 = 'Richness ~  A_mean_temp + A_rainfall'
y, X = patsy.dmatrices(f3, data, return_type='matrix')

model_3 = sm.GLM(y, X, family=fam).fit()
calculate_nested_f_statistic(model_3, model_2)

f4 = 'Richness ~  A_mean_temp + A_rainfall + C(Olsoneconame) + C(Ribeirovegtype)'
y, X = patsy.dmatrices(f1, data, return_type='matrix')

model_4 = sm.GLM(y, X, family=fam).fit()
calculate_nested_f_statistic(model_4, model_2)

f4 = 'Richness ~  A_mean_temp'
y, X = patsy.dmatrices(f4, data, return_type='matrix')

model_4 = sm.GLM(y, X, family=fam).fit()
calculate_nested_f_statistic(model_4, model_3)

f5 = 'Richness ~ 1'
y, X = patsy.dmatrices(f5, data, return_type='matrix')

model_5 = sm.GLM(y, X, family=fam).fit()
calculate_nested_f_statistic(model_5, model_4)

#%%
print(model_0.summary())

# %%
