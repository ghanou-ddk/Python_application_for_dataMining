# -*- coding: utf-8 -*-
"""
Created on Tue May 12 13:57:56 2020

@author: Ghanou
"""

#from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QAbstractTableModel, Qt
class MultiColumnLabelEncoder:

    def __init__(self, columns=None):
        self.columns = columns # array of column names to encode


    def fit(self, X, y=None):
        self.encoders = {}
        columns = X.columns if self.columns is None else self.columns
        for col in columns:
            self.encoders[col] = LabelEncoder().fit(X[col])
        return self


    def transform(self, X):
        output = X.copy()
        columns = X.columns if self.columns is None else self.columns
        for col in columns:
            output[col] = self.encoders[col].transform(X[col])
        return output


    def fit_transform(self, X, y=None):
        return self.fit(X,y).transform(X)


    def inverse_transform(self, X):
        output = X.copy()
        columns = X.columns if self.columns is None else self.columns
        for col in columns:
            output[col] = self.encoders[col].inverse_transform(X[col])
        return output


class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None
def getModel(df):
    model = pandasModel(df)
    return model

def dict_from__textfile(fname):
    
    with open(fname) as f:
        lines = f.readlines()

    c={}
    c1={}
    lines.remove('\n')
    for line in lines:
      

        if line[0]=='#':
             a,b=line.split('< ') 
    
        
        elif line=='\n':
            c[b[:-1]]=c1
            c1={}
        else:
            m,n=line.split('  ',1)#split first occurence only
            c1[m]=n[:-1]
    c[b[:-1]]=c1
    return c
def replacewith(df,dic1,selected):
                
    dic2={}
    df=df.applymap(str)
    for item in selected:
        dic2=dic1[item[1]]
        df[item[0]].replace(dic2, inplace=True)
    return df
def remove_selected_column(df,indexes):
    for index in sorted(indexes):
        col=df.columns[index.column()]

        del df[col]
    return df
def remove_selected_row(df,rows):
    for row in rows:
    
        df.drop(df.index[[row]])
        
    return df




#
def remove_rows_with_nan_values_at_selected_column(df,col):
    indx=[]
    for i in range(len( df[col])):
        
        if df[col].isnull().values[i]:
            indx.append(i)
    df=df.drop(df.index[indx]) 

    return df
def remove_column_more_than_k_nan_values(df,k):
    col=df.columns.values
    for i in col:
        if df[i].isnull().sum()/df.shape[0]>k:
                    del df[i]          
    return df

##### dtype=object ->  ->  pd.read_csv("DataCanReg.confirmes12Fev2020.csv",sep=',',na_values=np.nan ,dtype=object)
def missing_value_impute(df):
    #data frame frame values must be all string cause this one return only the string columns
    df=df.select_dtypes(include='object').fillna(df.select_dtypes(include='object').mode().iloc[0])
  ##for float values use(mean method) :df.select_dtypes(include='float').fillna(df.select_dtypes(include='float').mean().iloc[0])
    
    return df
def information_gain_calculate_only_integer(df,clas):
    from sklearn.feature_selection import mutual_info_classif


    res = dict(zip(['Name', 'Age','tall'],
               mutual_info_classif(df.iloc[:,0:2], df.iloc[:,2], discrete_features=True)
               ))
    return res    #res is dictionary canotain {'name of column' : IG ratio}
    

from sklearn.feature_selection import mutual_info_classif
from sklearn.preprocessing import LabelEncoder

def label_encoder_df(df):
    multi = MultiColumnLabelEncoder(columns=df.columns)
    df_temp = df.astype("str")
    
    df_temp = multi.fit_transform(df_temp)
    
    
    df_f = df_temp.where(~df.isna(), df)
    return multi,df_f


def reverse_label_encoder_df(multi,df):
    df=df.astype(int)
    df=multi.inverse_transform(df)
    return df

import pandas as pd
from missingpy import MissForest
def miss_forest_impute(df):
    imputer = MissForest(max_iter=3)
    imputer.fit(df,cat_vars=list(range(0,len(df.columns))))
    X_imputed = imputer.transform(df)
    df = pd.DataFrame(X_imputed,columns=df.columns)
    df.to_csv('temp_df.csv', sep=',')

    return df
from sklearn.ensemble import ExtraTreesClassifier

from sklearn.feature_selection import SelectKBest,chi2
from matplotlib import pyplot as plt

def information_gain_calculate(df,clas):
    X=df[df.columns.difference([clas])]
    Y=df[clas]
    model = ExtraTreesClassifier()
    model.fit(X,Y)
    print(model.feature_importances_) #use inbuilt class feature_importances of tree based classifiers
    #plot graph of feature importances for better visualization
    feat_importances = pd.Series(model.feature_importances_, index=X.columns)
    feat_importances.nlargest(20).plot(kind='barh')
    plt.savefig('graph_img_1.png')


    return feat_importances













