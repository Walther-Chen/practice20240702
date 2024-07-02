# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 15:16:34 2024

@author: Tristan
"""
import re
def ER_detector (text):
    ER_match=(re.search('ER \((.)*\)|ER\((.)*\)|ER\: \((.)*\)',text))
    try:
        ER_match=ER_match.group()
        ER_match=(re.search('.*?\)', ER_match))
        ER_match=ER_match.group()
    except AttributeError:
        pass
    return ER_match

def PR_detector (text):
    PR_match=(re.search('PR \((.)*\)|PgR \((.)*\)|PR\((.)*\)|PR\: \((.)*\)',text))
    try:
        PR_match=PR_match.group()
        PR_match=(re.search('.*?\)', PR_match))
        PR_match=PR_match.group()
    except AttributeError:
        pass
    return PR_match
