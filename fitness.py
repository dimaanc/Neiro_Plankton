import matplotlib.pyplot as plt
from sklearn import datasets
import pandas as pd
import numpy as np
anime = pd.read_csv('anime-recommendations-database/anime.csv')
rating = pd.read_csv('anime-recommendations-database/rating.csv')
anime_modified = anime.set_index('name')
import mpl_toolkits.mplot3d
digits = datasets.load_digits()



def fitness():
   M1 =data_macro['M1'].tolist()
   M2 =data_macro['M2'].tolist()
   M3 =data_macro['M3'].tolist()
   M4 =data_macro['M4'].tolist()
   M5 =data_macro['M5'].tolist()
   M6 =data_macro['M6'].tolist()
   M7 =data_macro['M7'].tolist()
   M8 =data_macro['M8'].tolist()
   J = []
foriin range(len(data_strat)):
      p =lam[0]*M1[i] + lam[2]*M3[i] + lam[3]*M4[i]
      q =lam[1]*M2[i]
      r =lam[4]*M5[i] + lam[6]*M7[i] + lam[7]*M8[i]
      s =lam[5]*M6[i]

if ((4*r*p + (p + q - s)**2) < 0):
J.append(0)
else:
         j =-s - p - q + (4*r*p + (p + q - s)**2)**0.5
J.append(j)
data=pd.read_csv('data_macro.csv')
data.insert(0, 'J', J)
#data = data.loc[data.J !=0]
#data = data.reset_index(drop=True)
data.to_csv('data_fit_macro.csv', index=False)
return data
