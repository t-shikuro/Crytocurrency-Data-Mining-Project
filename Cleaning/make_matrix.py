#%%
import pandas as pd
import numpy as np

#%%
df = pd.read_csv("fullset2.csv") # import the data
r = np.array(df['timestamp'].values, dtype='datetime64') # make sure date is correct dtype
df['timestamp'] = r  # reset the dataframe to the dtyped column
df = df[['timestamp', 'price', 'coin']]     # only what we need
df = df.sort_values(by = 'timestamp', axis=0)   # sort the dataframe values by date
unique = list(np.sort(np.unique(r),axis=0))     # create a list with all unique date values, and sort this list
df

#%%

l1 = np.empty(np.size(unique))        # make some lists of same size
l2 = np.empty(np.size(unique))        
l3 = np.empty(np.size(unique))
l4 = np.empty(np.size(unique))
l5 = np.empty(np.size(unique))
l1[:] = np.nan                        # nan fill
l2[:] = np.nan
l3[:] = np.nan
l4[:] = np.nan
l5[:] = np.nan
newframe = pd.DataFrame({'1' : l1, '2' : l2, '3': l3 , '4' : l4, '5': l5}, index = unique) # creating a dataframe with the unique date list as index

# %%
newframe
# %%
newframe = newframe.to_numpy()              # turn the blank dataframe into a numpy matrix
tup = [tuple(x) for x in df.values]         # turn all sorted data items into tuples

# %%
def makematrix(sometuple, somematrix, somelist):
    idx = 0
    for transaction in sometuple:  
        # iterate through the tuples
        date = somelist[idx]    # the first is going to match
        if date != transaction[0]:  # if the last date isnt correct, the very next date has to be
            idx = idx + 1
        # index into list
        somematrix[idx][transaction[2]-1] = transaction[1]
    return somematrix
# %%
#%time newframe = makematrix(tup, newframe, unique)  # to check how long it takes
newframe = makematrix(tup, newframe, unique)
# %%
r = pd.DataFrame(newframe, index = unique)
# %%
r.to_csv("matrix.csv")