import numpy as np
from scipy.stats import linregress
import math as m
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
from sklearn.linear_model import LinearRegression
from pylab import *
'''
"Boligareal"
"Grundareal"
"Liggetid"
"Kontantpris"
"NytBadevaerelse"
"AntalSovevaerelser"
"Salgsdato"
"Postnr"
plt.plot(df.Postnr,df.Kontantpris,'ob',alpha=.5, ms=20)


'''


df = pd.read_csv("/Users/ibrahimharas/Desktop/DV/project/home (1)/HOME.csv", delimiter = ';')
df.Kontantpris
'''
df.dropna()


def plot(column1,column2,EdType):
    x=df.groupby('EjdType')
    type=x.get_group(EdType)
    plt.plot(type[column1],type[column2],'r.',alpha=.38)
    plt.xlabel(column1)
    plt.ylabel(column2)
    plt.title(EdType)
'''
'''
    X=df[column1].values.reshape(-1,1)  #values converts it in to a numpy array
    Y=df[column2].values.reshape(-1,1)   #-1meansthatcalculatethedimensionofrows,buthave1column

    linear_regressor=LinearRegression()  #createobjectfortheclass
    linear_regressor.fit(X,Y)   #performlinearregression
    Y_pred=linear_regressor.predict(X)  #makepredictions

    #a=round(float(linear_regressor.coef_),2)
    #b=round(float(linear_regressor.intercept_),2)

    #title('Linearitet-{0}\nKontantpris={1:.2f}(0)+{2:.2f}'.format(column2,a,b))

    plt.plot(X,Y_pred,color='b')
'''




#plot("Kontantpris","Alder","Raekkehus")

#def plot2():
 #   x="Ejerlejlighed"
  #  y="Kontantpris"
    #plt.figure(x)
'''
    plt.subplot(2,2,1)
    plot("Alder",y,x)#alder
    plt.grid(True)

    plt.subplot(2,2,2)
    plot("Boligareal",y,x)#boligareal
    plt.grid(True)

    plt.subplot(2,2,3)
    plot("Grundareal",y,x)#Grundeareal
    plt.grid(True)

    plt.subplot(2,2,4)
    plot("Liggetid",y,x)#liggetid
    plt.grid(True)

    plt.show()
'''
'''
    plt.subplot(1,1,1)
    plot("Postnr",y,x)


    #plt.savefig("/Users/ibrahimharas/Desktop/CODE/piechertRækk.pdf")
    plt.title(x)

    plt.show()


plot2()

'''
#print(6/2)


