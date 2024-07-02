# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 15:13:20 2024

@author: Tristan
"""

import os
import csv
import ER_PR_detector as ep
import sys
path=sys.argv[0]

path = os.path.split(path)
path = path[0]
files= os.listdir(path)
with open(f'{path}\\storage.csv','w',newline='') as stor:
    names=['file','matched_text']
    writer=csv.DictWriter(stor,fieldnames=names)
    writer.writeheader()
    for j in files:
        if '.txt' in j:
            x=open(f'{path}\\{j}','r',encoding='utf-8')
            #initiate
            d=dict({'file':f'{j}','matched_text':[]})
            for i,element in enumerate(x.readlines(),start=1):
                
                #ER MATCH
                match_result= ep.ER_detector(element)
                if match_result != None:
                    d['matched_text'].append([i,match_result])
                
                #PR MATCH
                match_result= ep.PR_detector(element)
                if match_result != None:
                    d['matched_text'].append([i,match_result])
            writer.writerow(d)