# -*- coding: utf-8 -*-
"""
Created on Thu May  7 17:15:27 2020

@author: Ghanou
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 11:45:05 2020

@author: Ghanou
"""
import matplotlib.patches as mpatches
import random
import pandas as pd

from matplotlib import pyplot as plt
import numpy as np


def cancer_list_by_region(city_names,df,adr,local,filtre_nbcase):
  
    cancer_names=df[local]
    d1 = {}
    for w in cancer_names:
            d1[str(w)] = d1.get(str(w), 0) + 1
    for key, value in dict(d1).items():
        if value < filtre_nbcase:
            del d1[key]
    cancer_names=[*d1]#retieve al keys of dict as list
    c=[]
    c1=[]
    c2=[]
    c22=[]
    print(df.iloc[0][adr])
    for i in range(len(city_names)):
        for i2 in range(df.shape[0]):
                
                if df.iloc[i2][adr]==city_names[i]:
                    c2.append(df.iloc[i2][local])     #
        freqs = {}
        for w in c2:
            freqs[str(w)] = freqs.get(str(w), 0) + 1
        for key, value in freqs.items():
            c22.append([key, value])
        for i3 in range(len(cancer_names)):
                c1.append(freqs.get(cancer_names[i3], 0))# 
        c.append(c1)
        c1=[]
        c22=[]
        c2=[]
    return c,cancer_names
 ##############################################################       
def staticMap(city,dpi,df,adr,local,filtre_nbcase):
    with open('map/'+city+'_data.txt') as f:
        lines = f.readlines()
    city_names=lines[0][:-1].split(',')[1:]   
    xpos=lines[1][:-1].split(',')[1:]
    ypos=lines[2][:-1].split(',')[1:]
    population=lines[3].split(',')[1:]
    
    c_numbers,cancer_names=cancer_list_by_region(city_names,df,adr,local,filtre_nbcase)
    colors=[]
    for i in range(len(cancer_names)):
        colors.append('#'+str("%06x" % random.randint(0, 0xFFFFFF)))
    
    #fig, ax = plt.subplots() 
    im =plt.imread("map/"+str(city)+".png")
    im=np.flipud(im)#mirror image upside doown
    height, width, depth = im.shape
    figsize = width / float(dpi), height / float(dpi)
    fig = plt.figure(figsize=figsize)
    #plt = fig.add_axes([0, 0, 0.8, 0.8])
    vil =  city_names
    
    cancer=c_numbers
    red_patch=[]
    for i in range (len (xpos)):
        plt.pie(cancer[i], autopct='%1.2f%%',center=(int(xpos[i]),int(ypos[i])) ,
               radius=sum(cancer[i])*9800/float(population[i])+15,textprops={'fontsize': 0},colors=colors)
        plt.text(int(xpos[i])+90,int(ypos[i]), vil[i], size=10,
             ha="center", va="center",
             bbox=dict(boxstyle="round",
                       ec=(1., 0.5, 0.5),
                       fc=(1., 0.8, 0.8),
                       )
             )
    for i in range(len(cancer[0])):
        red_patch.append(mpatches.Patch(color=colors[i], label=cancer_names[i]))
    plt.legend(handles=red_patch)
    
    #ax.pie(students, labels = langs,autopct='%.1f%%',center=(3,3),radius=4)
    #ax.pie(students, labels = langs,autopct='%1.2f%%',center=(8,2),radius=4)
    plt.imshow(im)
    plt.axis('equal')
    plt.savefig('img.png')
    
    
def graph(df, x_dim, y_dim):
  x = df[x_dim]
  y = df[y_dim]
  fig, ax = plt.subplots(figsize=(10, 5))
  #customizes alpha for each dot in the scatter plot
  ax.scatter(x, y, alpha=0.60)
 
  #adds a title and axes labels
  ax.set_title('example')
  ax.set_xlabel(x_dim)
  ax.set_ylabel(y_dim)
 
  #removing top and right borders
  ax.spines['top'].set_visible(False)
  ax.spines['right'].set_visible(False)
  #adds major gridlines
  ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
  plt.savefig('graph_img.png')
#  plt.show()

