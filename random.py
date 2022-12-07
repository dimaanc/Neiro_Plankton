import matplotlib.pyplot as plt
from sklearn import datasets
import pandas as pd
import numpy as np
digits = datasets.load_digits()


def strategy(Nmax):
defrand_strat_A():
        A = []
foriin range(0, Nmax):
            a =rn.randint(-D*100, 0)
A.append(a)
return A
defrand_strat_B(a):
        A, B = [], []
foriin range(0, Nmax):
            b =rn.randint(-min(-a[i], a[i] + D*100), 0)
A.append(a[i]/100)
B.append(b/100)
A.append(a[i]/100)
B.append(-b/100)
return A, B

    a =rand_strat_A()
    A, B =rand_strat_B(a)
    data_strat1 = {'Aj': A, 'Bj': B}
    data1 =pd.DataFrame(data = data_strat1)
    a =rand_strat_A()
    A, B =rand_strat_B(a)
    data_strat2 = {'Aa': A, 'Ba': B}
    data2 =pd.DataFrame(data = data_strat2)
data=pd.concat([data1, data2], axis=1)
data.to_csv("data_strat.csv", index=False)
return data

data_strat=strategy(Nmax)
data_strat
