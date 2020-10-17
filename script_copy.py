# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:56:19 2019

@author: wwech
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 23:36:29 2019

@author: wwech
"""
import sys
import requests
import re
import shutil
from bs4 import BeautifulSoup 
 
url = "http://www.imfdb.org/wiki/Main_Page"

def get_source(url):
    r = requests.get(url)
    if r.status_code == 200:
        return BeautifulSoup(r.text,"html.parser")
    else:
        sys.exit( "[~] Invalid Response Received." )

html = get_source(url) 

html

def html_tag_filter( html, tag, attrs = None ):
    tags = html.findAll(tag,attrs)
    if tags:
        return tags
    else:
        sys.exit("[~] No tags detected on the page.")

attrs = {"id":"mp-secondbanner"}

table_tag = html_tag_filter(html, "table", attrs)

links = []

for a in table_tag[0].find_all('a', href=True):
    links.append("http://www.imfdb.org"+a['href'])
    
links.pop(0)
links

inner_links = []

for l in links:
    inner_html = get_source(l)
    inner_table_tag = html_tag_filter(inner_html,"table",{'class':'mw-allpages-table-chunk'})    
    for a in inner_table_tag[0].find_all('a', href=True):
        inner_links.append("http://www.imfdb.org"+a['href'])

inner_links[:10]

from tqdm import tqdm
import os
import threading

THREAD_COUNTER = 0
THREAD_MAX     = 5

os.mkdir( os.path.join( os.getcwd(), 'images' ) )

def requesthandle( link, name ):
    r = requests.get( link, stream=True )
    if r.status_code == 200:
        r.raw.decode_content = True
        f = open( "new/"+name, "wb" )
        shutil.copyfileobj(r.raw, f)
        f.close()
        print("[*] Downloaded Image: %s" % name)
        
img_src = []
img_link = []
for l in tqdm(inner_links[:5]):
    inner_html = get_source(l)
    imgs = inner_html.findAll( "img" , attrs={'class': 'thumbimage'})
    for img in imgs:
        src = img.get( "src" )
        if src:
            src = re.match( r"((?:https?:\/\/.*)?\/(.*\.(?:jpeg|jpg)))", src )
            if src:
                img_src.append(src)
                (link, name) = src.groups()
                if link:
                    link = "http://www.imfdb.org"+link
                    img_link.append(link)
                    _t = threading.Thread( target=requesthandle, args=(link, name.split("/")[-1]) )
                    _t.daemon = True
                    _t.start()
                    while THREAD_COUNTER >= THREAD_MAX:
                        pass
                
while THREAD_COUNTER > 0:
        pass
                
(l,n) = img_src[0].groups()
n.split('/')[-1]
img_link[0]
"""
inner_r = requests.get( src, stream=True )
                if inner_r.status_code == 200:
                    inner_r.raw.decode_content = True
                    f = open( name.split("/")[-1], "wb" )
                    shutil.copyfileobj(inner_r.raw, f)
                    f.close()
            
"""