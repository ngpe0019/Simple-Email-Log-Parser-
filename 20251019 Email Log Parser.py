# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 20:08:29 2025

@author: joeyj
"""

mbox=input('insert your email log txt:')
mbox=open(mbox)
email=[]
day=[]



for f in mbox:
    f=f.rstrip()
    f=f.lower()
    if f.startswith('from '):
        g=f.split()
        email.append(g[1])
        day.append(g[2].capitalize())
        #print(email)
        #print(day)
    else:
        continue
    
email_d=dict()
day_d=dict()

for e in email:
    email_d[e]=email_d.get(e,0)+1

for d in day:
    day_d[d]=day_d.get(d,0)+1
    
print('this dictionary shows email and frequency:')
print(email_d)
print('this dictionary shows day and frequency:')
print(day_d)
    