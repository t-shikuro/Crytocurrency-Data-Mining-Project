#%%
import seaborn as sns; sns.set(style="ticks", color_codes=True)
import statsmodels.formula.api as smf
import pandas as pd
import numpy as np
import statsmodels.api as sm
#%%
x = pd.read_csv('matrix_second_filledforward.csv', index_col = "time") # read out data
y = pd.read_csv("normalizedmatrix.csv")
#x = x.fillna(method='ffill')  #forward fills values
y = y.fillna(method='ffill')
x = x[["bch","btc","eth","ltc","xrp"]]
y = y[["bch","btc","eth","ltc","xrp"]]
#%%
y.to_csv("norm_matrix_filledforward.csv")
#%%
x.describe(include="all")
#%%
y
#%%
y.describe(include="all")
# %%
model_trn = smf.ols(formula='bch~btc+eth+ltc+xrp', data=x).fit()
model_trn.summary()
# %%
model_trn = smf.ols(formula='btc~bch+eth+ltc+xrp', data=x).fit()
model_trn.summary()
# %%
model_trn = smf.ols(formula='eth~btc+bch+ltc+xrp', data=x).fit()
model_trn.summary()
# %%
model_trn = smf.ols(formula='ltc~btc+bch+eth+xrp', data=x).fit()
model_trn.summary()
# %%
model_trn = smf.ols(formula='xrp~btc+bch+ltc+eth', data=x).fit()
model_trn.summary()
# %%
l = sns.pairplot((x), kind='reg', markers="+") # get some graphical info
l = l.fig
l.savefig("pairplot.png")

# %%
test = model_trn.predict(x)
real = x['ltc']

# %%
print(test)
# %%
print(real)

# %%
avg = 0
goodnum = 0
for idx, list1 in enumerate(test.values):
    if not np.isnan(list1) and not np.isnan(real[idx]):
        goodnum = goodnum + 1
        #print(list1,real[idx])
        avg = avg + (abs(list1-real[idx])/real[idx])
        #print(abs(list1-real[idx])/real[idx])

# %%
print(avg/ goodnum)

# %%
