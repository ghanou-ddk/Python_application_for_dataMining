# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 18:55:00 2020

@author: Ghanou
"""
from sklearn.model_selection import KFold

from sklearn.tree import DecisionTreeClassifier 
from sklearn import tree
from sklearn.metrics import confusion_matrix 
from sklearn.preprocessing import LabelEncoder

from sklearn import datasets 
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn import svm
from sklearn.metrics import classification_report

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import ShuffleSplit
from sklearn.neural_network import MLPClassifier
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


def label_encoder_df(df):
    multi = MultiColumnLabelEncoder(columns=df.columns)
    df_temp = df.astype("str")
    
    df_temp = multi.fit_transform(df_temp)
    
    
    df_f = df_temp.where(~df.isna(), df)
    return multi,df_f

def get_confusion_matrix_values(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)
    return(cm[0][0], cm[0][1], cm[1][0], cm[1][1])

def svm_dm(df,features,clas,split,k):
    specificity=[]
    accuracy=[]
    sensitivity=[]
    m,df=label_encoder_df(df)
    print(clas,split,features)
    res=[]
    clf = svm.SVC(kernel='rbf')
    
    X=df[features]
    Y=df[clas]
    kf =KFold(n_splits=k, random_state=None, shuffle=True)
    
    res=[]
    for train_index, test_index in kf.split(X):
        # print("TRAIN:", train_index, "TEST:", test_index)
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
        tn, fp, fn, tp = get_confusion_matrix_values(y_te, p)
        print(tn)
        print(tp)
        print(fn)
        print(fp)

        specificity.append( tn / (tn+fp))
        accuracy.append( (tn + tp)/(tn+tp+fn+fp))
        sensitivity.append( tp/(tp + fn))
        e1=np.array(accuracy)
        e2=np.array(sensitivity)
        #e3=np.array(precesion)
        e4=np.array(specificity)


    res2=("SVM:                 %0.2f ± %0.2f" % (e1.mean(),e1.std())+"    %0.2f ± %0.2f" % (e2.mean(),e2.std())+"       %0.2f ± %0.2f" % (e4.mean(),e4.std())+"\n")

    res=np.array(res)
    res1="Accuracy: %0.2f (+/- %0.2f)" % (res.mean(), res.std() * 2)
    print(res1) 
    #res2=t# accuracy sensitivity ... ect

    return res2,res1,m,clf     

    ###method 1
    # cv = ShuffleSplit(n_splits=k, test_size=split/100, random_state=0)
    # scores=cross_val_score(clf, X, Y, cv=cv)
    # res="Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2)
    
    ###method 2
    # KFold(n_splits=5, random_state=None, shuffle=False)
    # kf = KFold(n_splits=5)
    # print(len(X))
    # print(len(Y))
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
    #     res.append('Number of correctly classified instances:       '+str(t)+'     '+str(100*t/len(y_te))[:5]+'%'+'\nNumber of incorrectly classified instances:     '+str(len(y_te)-t)+'     '+str(100*(len(y_te)-t)/len(y_te))[:5]+        '%\nTotal number of instances:                      '+str(len(y_te)) +'\n' + classification_report(y_te, p,labels=[1, 2, 3],zero_division=0) )
    # # clf.fit(x_tr, y_tr)
    # # p=clf.predict(x_te)
    # # y_te.reset_index(inplace=True, drop=True)
    # # t=0
    # # for i in range(len(y_te)):
    # #     # print(i)
    # #     if y_te[i]==p[i]:
    # #         t+=1
    # # res='Number of correctly classified instances:       '+str(t)+'     '+str(100*t/len(y_te))[:5]+'%'+'\nNumber of incorrectly classified instances:     '+str(len(y_te)-t)+'     '+str(100*(len(y_te)-t)/len(y_te))[:5]+        '%\nTotal number of instances:                     '+str(len(y_te)) +'\n' + classification_report(y_te, p,labels=[1, 2, 3])   



# def kmeans(data,nbc,features):
#     y = datasets.load_iris()['target']
#     x = datasets.load_iris()['data']
     
#     kmeans = KMeans(n_clusters=3) 
#     p=kmeans.fit_predict(x)
#     correct=0
#     for i in range(len(p)):
#         if p[i]==y[i]:
#             correct+=1
        
#     print(correct/len(p))


def decesion_tree(df,features,clas,split,k):
    m,df=label_encoder_df(df)
    specificity=[]
    accuracy=[]
    sensitivity=[]
    clas='SUIVI'
    X=df[df.columns.difference([clas,'Unnamed: 0'])]
    Y=df[clas]
    clf = DecisionTreeClassifier(random_state=3,max_depth=7,criterion = "entropy")
    score=cross_val_score(clf, X, Y, cv=10)
    print("Accuracy: %0.2f (+/- %0.2f)" % (score.mean(), score.std() * 2))
    cont=0

    print(score)
    res=[]
    kf =KFold(n_splits=k, random_state=None, shuffle=True)
    for train_index, test_index in kf.split(X):
        cont+=1
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
        tn, fp, fn, tp = get_confusion_matrix_values(y_te, p)
        specificity.append( tn / (tn+fp))
        accuracy.append( (tn + tp)/(tn+tp+fn+fp))
        sensitivity.append( tp/(tp + fn))
        e1=np.array(accuracy)
        e2=np.array(sensitivity)
        #e3=np.array(precesion)
        e4=np.array(specificity)


    res2=("decesion tree:     %0.2f ± %0.2f" % (e1.mean(),e1.std())+"    %0.2f ± %0.2f" % (e2.mean(),e2.std())+"       %0.2f ± %0.2f" % (e4.mean(),e4.std())+"\n")

    res=np.array(res)
    res1="Accuracy: %0.2f (+/- %0.2f)" % (res.mean(), res.std() * 2)
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(55, 20))
    
    tree.plot_tree(clf,feature_names=df.columns.difference([clas]),class_names=['Alive','Dead'],rounded=True,filled=True,fontsize=12)
    plt.savefig('graph_img_1.png')
    plt.show()
    
   #res2=t# accuracy sensitivity ... ect
    return res2,res1,m,clf
def neural_network(df,features,clas,split,k):
    m,df=label_encoder_df(df)
    specificity=[]
    accuracy=[]
    sensitivity=[]
    clas='SUIVI'
    X=df[df.columns.difference([clas,'Unnamed: 0'])]
    Y=df[clas]
    clf = MLPClassifier(random_state=1, max_iter=300)
    score=cross_val_score(clf, X, Y, cv=10)
    print("Accuracy: %0.2f (+/- %0.2f)" % (score.mean(), score.std() * 2))
    cont=0

    print(score)
    res=[]
    kf =KFold(n_splits=k, random_state=None, shuffle=True)
    for train_index, test_index in kf.split(X):
        cont+=1
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
        tn, fp, fn, tp = get_confusion_matrix_values(y_te, p)
        specificity.append( tn / (tn+fp))
        accuracy.append( (tn + tp)/(tn+tp+fn+fp))
        sensitivity.append( tp/(tp + fn))
        e1=np.array(accuracy)
        e2=np.array(sensitivity)
        #e3=np.array(precesion)
        e4=np.array(specificity)


    res2=("neural network:   %0.2f ± %0.2f" % (e1.mean(),e1.std())+"    %0.2f ± %0.2f" % (e2.mean(),e2.std())+"       %0.2f ± %0.2f" % (e4.mean(),e4.std())+"\n")

    res=np.array(res)
    res1="Accuracy: %0.2f (+/- %0.2f)" % (res.mean(), res.std() * 2)
       
    #res2=t# accuracy sensitivity ... ect
    return res2,res1,m,clf

# svm
# >>> from sklearn import svm
# >>> X = [[0, 0], [1, 1]]
# >>> y = [0, 1]
# >>> clf = svm.SVC()
# >>> clf.fit(X, y)
# >>> clf.predict([[2., 2.]])



