# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 15:55:00 2019

@author: wwech
"""

import sys
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup 
from tqdm import tqdm
import pandas as pd
url = "http://www.imfdb.org/wiki/Category:Gun"

def get_source(url):
    r = requests.get(url)
    if r.status_code == 200:
        return BeautifulSoup(r.text,"html.parser")
    else:
        sys.exit( "[~] Invalid Response Received." )


def html_tag_filter( html, tag, attrs = None ):
    tags = html.findAll(tag,attrs)
    if tags:
        return tags
    else:
        sys.exit("[~] No tags detected on the page.")
        

titles = []

def extract_titles(url):
    next_link = None
    attrs = {"id":"mw-pages"}
    outer_div = html_tag_filter(get_source(url), "div", attrs)
    inner_div = outer_div[0].findAll("div", {'class':'mw-content-ltr'})
    for a in tqdm(inner_div[0].findAll('a', href=True)):
        titles.append(a['href'].split('/')[-1])
    try:
        next_link = 'http://www.imfdb.org/'+outer_div[0].findAll('a', href=True)[-1]['href']
        if next_link is not None:
            extract_titles(next_link)
        else:
            print('No link found')
    except Exception as e:
        print(e)
            
extract_titles(url)    
 
titles = list(set(titles))
len(temp)

import pandas as pd
df = pd.DataFrame(titles,columns = ['titles']) 
df.to_csv (r'gun_titiles.csv', header=True)
with open('gun_titles.csv','a') as f:
    f.write('title,%s\n'%(titles))
    f.flush()