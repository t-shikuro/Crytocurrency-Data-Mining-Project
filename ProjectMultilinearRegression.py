#%%
import seaborn as sns 
import statsmodels.formula.api as smf
import pandas as pd
import numpy as np
import statsmodels.api as sm
#%%
x = pd.read_csv('fullsetmatrix1.csv', index_col = "Time") # read out data
y = pd.read_csv("normalizedmatrix.csv")
r = x[["bch","btc","eth","ltc","xpr"]]
y = y[["bch","btc","eth","ltc","xpr"]]
#%%
r
#%%
r.describe(include="all")
#%%
y.describe(include="all")
#%%
y

# %%
model_trn = smf.ols(formula='bch~btc+eth+ltc+xpr', data=x).fit()
model_trn.summary()
# %%
model_trn = smf.ols(formula='btc~bch+eth+ltc+xpr', data=x).fit()
model_trn.summary()
# %%
model_trn = smf.ols(formula='eth~btc+bch+ltc+xpr', data=x).fit()
model_trn.summary()
# %%
model_trn = smf.ols(formula='ltc~btc+bch+eth+xpr', data=x).fit()
model_trn.summary()
# %%
model_trn = smf.ols(formula='xpr~btc+bch+ltc+eth', data=x).fit()
model_trn.summary()


# %%
l = sns.pairplot((r), diag_kind='kde') # get some graphical info
l = l.fig
l.savefig("pairplot.png")



# %%
