# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 14:31:09 2020

@author: Ghanou
"""
from sklearn.model_selection import KFold
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import numpy as np
from sklearn.metrics import classification_report
from sklearn.feature_selection import SelectKBest,f_classif
from sklearn import svm
df= pd.read_csv("temp_df.csv",sep=',',na_values='na',dtype=object)

clas='SUIVI'
X=df[df.columns.difference([clas,'Unnamed: 0'])]
Y=df[clas]

print(0000000000000000000000000000000,'\n\n')
# clf = svm.SVC(kernel='rbf',C=10000,gamma=0.001)

# kf =KFold(n_splits=3, random_state=None, shuffle=True)

# res=[]
# for train_index, test_index in kf.split(X):
#     # print("TRAIN:", train_index, "TEST:", test_index)
#     x_tr, x_te = X.iloc[train_index], X.iloc[test_index]
#     y_tr, y_te = Y[train_index], Y[test_index]
#     clf.fit(x_tr, y_tr)
#     p=clf.predict(x_te)
#     t=0
#     y_te.reset_index(inplace=True, drop=True)
#     for i in range(len(y_te)):
#         if y_te[i]==p[i]:
#             t+=1
    
#     rr=('Number of correctly classified instances:       '+str(t)+'     '+str(100*t/len(y_te))[:5]+'%'+'\nNumber of incorrectly classified instances:     '+str(len(y_te)-t)+'     '+str(100*(len(y_te)-t)/len(y_te))[:5]+        '%\nTotal number of instances:                      '+str(len(y_te)) +'\n' + classification_report(y_te, p,labels=[1, 2, 3],zero_division=0) )
#     print(rr)
#     res.append(t/len(y_te))
# res=np.array(res)
# print("Accuracy: %0.2f (+/- %0.2f)" % (res.mean(), res.std() * 2))

from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier


clf = DecisionTreeClassifier(random_state=3,max_depth=7,criterion = "entropy")
score=cross_val_score(clf, X, Y, cv=10)
print("Accuracy: %0.2f (+/- %0.2f)" % (score.mean(), score.std() ))

print(score)
res=[]
kf =KFold(n_splits=10, random_state=None, shuffle=True)
for train_index, test_index in kf.split(X):
    x_tr, x_te = X.iloc[train_index], X.iloc[test_index]
    y_tr, y_te = Y[train_index], Y[test_index]
    clf.fit(x_tr, y_tr)
    p=clf.predict(x_te)
    t=0
    y_te.reset_index(inplace=True, drop=True)
    for i in range(len(y_te)):
        if y_te[i]==p[i]:
            t+=1
    
    rr=('Number of correctly classified instances:       '+str(t)+'     '+str(100*t/len(y_te))[:5]+'%'+'\nNumber of incorrectly classified instances:     '+str(len(y_te)-t)+'     '+str(100*(len(y_te)-t)/len(y_te))[:5]+        '%\nTotal number of instances:                      '+str(len(y_te)) +'\n' + classification_report(y_te, p,labels=[1, 2, 3],zero_division=0) )
    print(rr)
    res.append(t/len(y_te))
res=np.array(res)
print("Accuracy: %0.2f (+/- %0.2f)" % (res.mean(), res.std() * 2))


# from sklearn import preprocessing
# label_encoder = preprocessing.LabelEncoder()
# m,df=dataPreparation.label_encoder_df(df)
# X=df[df.columns.difference([clas,'Unnamed: 0'])]
# Y=df[clas]




# import matplotlib.pyplot as plt
# fig, ax = plt.subplots(figsize=(40, 5))
# from sklearn import tree

# tree.plot_tree(clf,feature_names=df.columns.difference([clas]),class_names=['Alive','Dead'],rounded=True,filled=True,fontsize=12)

# plt.show()
























