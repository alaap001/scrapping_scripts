# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 14:28:02 2019

@author: wwech

()
"""

import pandas as pd
import os
import shutil

df = pd.read_csv('..\\movie_titles.csv')
count = 0
titles = list(set(df['titles']))
human_dir = [x[2] for x in os.walk(r'C:\Users\wwech\Desktop\vidooly stuff\weapon_dataset_alaap\train\Unsafe')]
other_dir = [x[0] for x in os.walk(r'C:\Users\wwech\Desktop\vidooly stuff\weapon_dataset_alaap\output_gun\others')]
#
#def intersection(lst1, lst2): 
#    return list(set(lst1) & set(lst2))
#    
#all_dirs = intersection(cur_dirs,titles)
#print(len(all_dirs))
#
#len(titles)
human_weapons = []
others = []
for cat in other_dir[1:]:
    for img in os.walk(cat):
        for i in img[2]:
            human_weapons.append(i)
            
human_weapons = list(set(human_weapons))
others = list(set(others))

for cat in other_dir[1:]:
    try:
        for img in os.walk(cat):
            for i_name in img[2]:
                source = img[0]+'\\'+i_name
                destination = r'C:\Users\wwech\Desktop\vidooly stuff\weapon_dataset_alaap\Guns'
                try:
                    shutil.move(source, destination)
                except Exception as e:
                    print(e)
    except Exception as e:
        print(e)
        
        
import os
        
i = 0
for fname in (os.listdir(r'./weapon_dataset_alaap/test/Safe')):
    reqd_fname = 'safe_img' + str(i) + '.jpg'
    src = r'./weapon_dataset_alaap/test/Safe/' + fname
    dst = r'./weapon_dataset_alaap/test/Safe/' + reqd_fname
    os.rename(src, dst)
    i += 1
    
    
for img in human_dir:
    for i_name in img[10000:]:
        source = r'C:\Users\wwech\Desktop\vidooly stuff\weapon_dataset_alaap\train\Unsafe'+'\\'+i_name
        destination = r'C:\Users\wwech\Desktop\vidooly stuff\weapon_dataset_alaap\train\Unsafe 2'
        try:
            shutil.copy(source, destination)
        except Exception as e:
            print(e)  
        

from math import exp,log

def ran_percent(v,l = 0,h = 0):
    v_ = log(v,58)
    re = 1/(1+exp(-v_))
    if v < 70000:
        return re - .50
    else:
        return re

ran_percent(20000)
   
x = []
y = []
for i in range(200000,20000000,200):
    x.append(i)
    y.append(ran_percent(i))
    
import matplotlib.pyplot as plt

plt.plot(x,y)


def clamp( x,  lowerlimit,  upperlimit):
    if (x < lowerlimit):
        x = lowerlimit
    if (x > upperlimit):
        x = upperlimit
    return x 

def smoothstep(edge0, edge1, x):
    # Scale, bias and saturate x to 0..1 range
    x = clamp((x - edge0) / (edge1 - edge0), 0.0, 1.0) 
    # Evaluate polynomial
    return x * x * x * (x * (x * 6 - 15) + 10)

smoothstep(20000,2000000,200000)

def sigmoid(x,mi, mx): 
    return mi + (mx-mi)*(lambda t: (1+200**(-t+0.5))**(-1) )( (x-mi)/(mx-mi) )    

sigmoid(2000000,200000,20000000)
import numpy as np

def smoothclamp(x, mi, mx): 
    return mi + (mx-mi)*(lambda t: np.where(t < 0 , 0, np.where( t <= 1 , 3*t**2-2*t**3, 1 ) ) )( (x-mi)/(mx-mi) )    
    
smoothclamp(200000,200,2000000)

    
    
    
    
    
    
    
    
    
    
    
    