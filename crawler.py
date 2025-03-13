# -*- coding: utf-8 -*-
"""
@author: jdwang@asia.edu.tw 
2019.5.26
"""

from bs4 import BeautifulSoup
import requests

import os

url='http://fpsother.tripod.com/yi/content.htm'

html = requests.get(url)
html.encoding = 'big5'
#print (html.text)

sp = BeautifulSoup(html.text,"html.parser")

Dir_Content = "Novels_Content_107021034"

if not os.path.exists(Dir_Content):
    os.mkdir(Dir_Content)
else:
    print(Dir_Content+"已經存在")

url_Base='http://fpsother.tripod.com/yi/'

links = sp.find_all(["a"])
for link in links:
    One_Title = link.text
    href=link.get("href")
    Except_href = 'http'
    mailto='mailto'
    if (Except_href in href or mailto in href) :
        print ("Not included=>"+ href )
    else:
        #print ("include=>"+link.text)
        One_Article_url = url_Base+href
        print (url_Base+href)
        One_Article_html = requests.get(One_Article_url)
        One_Article_html.encoding = 'big5'
        
        
        One_Article_sp = BeautifulSoup(One_Article_html.text,"html.parser")

        #print (One_Article_sp.text)
        # Generating the filename automatically.
        href_txt = href.replace(".htm","") # "01.htm"=>"01" 
        FileName = Dir_Content+"/"+href_txt+'_倚天屠龍記_'+One_Title+".txt"
        #print (FileName)
        
        # Output the content of the web page to a file
        #One_Article_Binary = One_Article_sp.text.encode('big5','ignore')
        
        f = open (FileName,'wb')
        all_pp =One_Article_sp.find_all(['p'])
        for one_p in all_pp:
            if not(Except_href in one_p or mailto in one_p):
                print(one_p.text)
                f.write(one_p.text.encode('big5','ignore'));
        f.close()
        
#import os

inputfilename = "./Novels_Content_107021034/04_倚天屠龍記_字作喪亂意彷徨.txt"
inputsss="./output.txt"
Word_freq = {}
Word_freq2 = {}
Totol_lines =""
with open (inputfilename,'r',encoding = 'big5') as File_In:
    while True:
        one_line = File_In.read()

        for c in one_line:
            if c not in Word_freq:
                Word_freq[c] = 1
            else:
                Word_freq[c] = Word_freq[c] +1   
#        print (one_line, sep='', end='')
        #priut (one_line)
        if not one_line:
            break
        Totol_lines += one_line
with open (inputsss,'r',encoding = 'big5') as File_In:
    while True:
        one_line1 = File_In.read()

        for c in one_line1:
            if c not in Word_freq2:
                Word_freq2[c] = 1
            else:
                Word_freq2[c] = Word_freq2[c] +1   
#        print (one_line, sep='', end='')
        #priut (one_line)
        if not one_line1:
            break
        Totol_lines += one_line1        
        
##print ("Total cnt :", len(Totol_lines))
Dir_Content = "Output_Frequency_107021034"

if not os.path.exists(Dir_Content):
    os.mkdir(Dir_Content)
else:
    print(Dir_Content+"已經存在")

outputfilename = Dir_Content+"/TestFile_1_WordFrequency.txt"
outputfilename2 = Dir_Content+"/TestFile_2_WordFrequency2.txt"


fo = open (outputfilename,'w',encoding='big5')
fa = open (outputfilename2,'w',encoding='big5')
for key in sorted(Word_freq,key=Word_freq.get,reverse=True):
    print ('%10s:%10d' % (key,Word_freq[key] ))
    if key in Word_freq2:
        fo.write('%s\t%d\n' % (key,Word_freq[key] ))
    else:
        fa.write('%s\t%d\n' % (key,Word_freq[key] ))

fo.close()
