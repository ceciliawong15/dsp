import pandas as pd
import numpy as np
data = pd.read_csv('faculty.csv')

Q1. Find how many different degrees there are, and their frequencies: 
Ex: PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

>>data[' degree'].nunique()
11

>>> data[' degree'].value_counts()
 Ph.D.                 15
 PhD                    7
 Sc.D.                  4
 Ph.D                   4
 JD MA MPH MS PhD       1
 ScD                    1
Ph.D.                   1
 B.S.Ed. M.S. Ph.D.     1
 PhD ScD                1
0                       1
 MD MPH Ph.D            1
 
Q2. Find how many different titles there are, and their frequencies: 
Ex: Assistant Professor, Professor

>>> data[' title'].nunique()
4

>>> data[' title'].value_counts()
Professor of Biostatistics              13
Associate Professor of Biostatistics    12
Assistant Professor of Biostatistics    11
Assistant Professor is Biostatistics     1
Name:  title, dtype: int64

Q3. Search for email addresses and put them in a list. 
Print the list of email addresses.


>>> list = data[' email']
>>> list
0     bellamys@mail.med.upenn.edu
1                warren@upenn.edu
2               bryanma@upenn.edu
3              jinboche@upenn.edu
4              sellenbe@upenn.edu
5     jellenbe@mail.med.upenn.edu
6               ruifeng@upenn.edu
7     bcfrench@mail.med.upenn.edu
8              pgimotty@upenn.edu
9         wguo@mail.med.upenn.edu
10        hsu9@mail.med.upenn.edu
11       rhubb@mail.med.upenn.edu
12      whwang@mail.med.upenn.edu
13      mjoffe@mail.med.upenn.edu
14    jrlandis@mail.med.upenn.edu
15            liy3@email.chop.edu
16     mingyao@mail.med.upenn.edu
17              hongzhe@upenn.edu
18             rlocalio@upenn.edu
19    nanditam@mail.med.upenn.edu
20    knashawn@mail.med.upenn.edu
21     propert@mail.med.upenn.edu
22       mputt@mail.med.upenn.edu
23             sratclif@upenn.edu
24             michross@upenn.edu
25       jaroy@mail.med.upenn.edu
26     msammel@cceb.med.upenn.edu
27                shawp@upenn.edu
28        rshi@mail.med.upenn.edu
29       hshou@mail.med.upenn.edu
30     jshults@mail.med.upenn.edu
31    alisaste@mail.med.upenn.edu
32     atroxel@mail.med.upenn.edu
33       rxiao@mail.med.upenn.edu
34        sxie@mail.med.upenn.edu
35                 dxie@upenn.edu
36     weiyang@mail.med.upenn.edu

Q4. Find how many different email domains there are 
(Ex: mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.). 
Print the list of unique email domains.

email = data[' email']
email = email.reset_index()
email['domain'] = 1
email['domain2'] = 1

email['domain'] = email[' email'].str.split('@')
domainlist = email['domain']
domainlist = [v for i,v in domainlist]
email['domain2'] = domainlist
>>> email['domain2'].value_counts()
mail.med.upenn.edu    23
upenn.edu             12
cceb.med.upenn.edu     1
email.chop.edu         1
Name: domain2, dtype: int64
