import matplotlib.pyplot as plt
from sklearn import datasets
import pandas as pd
import numpy as np
anime = pd.read_csv('anime-recommendations-database/anime.csv')
rating = pd.read_csv('anime-recommendations-database/rating.csv')
anime_modified = anime.set_index('name')
import mpl_toolkits.mplot3d
digits = datasets.load_digits()


defmacroparams(data_strat):
Aj=data_strat['Aj'].tolist()
Bj=data_strat['Bj'].tolist()
   Aa =data_strat['Aa'].tolist()
   Ba =data_strat['Ba'].tolist()
collect= defaultdict(list)
collect_M=defaultdict(list)
collect_MM=defaultdict(list)
foriin range(len(data_strat)):
collect['M1'].append(sigma1*(Aj[i] + D))
collect['M5'].append(sigma1*(Aa[i] + D))

collect['M2'].append(-sigma2*(Aj[i] + D +Bj[i]/2))
collect['M6'].append(-sigma2*(Aa[i] + D + Ba[i]/2))

collect['M3'].append(-2*(np.pi)*(np.pi)*Bj[i]*Bj[i])
collect['M7'].append(-2*(np.pi)*(np.pi)*Ba[i]*Ba[i])

collect['M4'].append(-((Aj[i] + D0)*(Aj[i] + D0) + (Bj[i]*Bj[i])/2))
collect['M8'].append(-((Aa[i] + D0)*(Aa[i] + D0) + (Ba[i]*Ba[i])/2))

foriin range(1, 9):
for j in range(1, 9):
ifi== j == 1 ori== j == 5:
            Z =np.array(collect['M' +str(i)])*np.array(collect['M' +str(j)])
collect_M['M' +str(i) + 'M' +str(j)].append(list(Z))
elifi== j:
            Z =-np.array(collect['M' +str(i)])*np.array(collect['M' +str(j)])
collect_M['M' +str(i) + 'M' +str(j)].append(list(Z))
else:
continue

foriin range(2, 9):
for j in range(1, i):
ifi== 5 and j == 1:
            Z = 2*np.array(collect['M' +str(i)])*np.array(collect['M' +str(j)])
collect_MM['M' +str(i) + 'M' +str(j)].append(list(Z))
else:
            Z =-np.abs(2*np.array(collect['M' +str(i)])*np.array(collect['M' +str(j)]))
collect_MM['M' +str(i) + 'M' +str(j)].append(list(Z))

data_macro= {}   
data=pd.DataFrame(data =data_macro)
foriin range(1, 9):
data['M' +str(i)] = collect['M' +str(i)]
foriin range(1, 9):
for j in range(1, 9):
ifi== j:
            data['M' +str(i) + 'M' +str(j)] =collect_M['M' +str(i) + 'M' +str(j)][0]
else:
continue
foriin range(2, 9):
for j in range(1, i):
         data['M' +str(i) + 'M' +str(j)] =collect_MM['M' +str(i) + 'M' +str(j)][0]
data.to_csv("data_macro.csv", index=False)
return data
data_macro=macroparams(data_strat)
data_macro

