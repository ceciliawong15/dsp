##Dictionary Python Part 2

###First Dict

import pandas as pd
data = pd.read_csv('faculty.csv')
data['splitname'] = data['name'].str.split(' ')
data['lastname'] = [i[-1] for i in data['splitname']]

###drop unnecessary columns and reorg DF

data.drop(data.columns[[0]], axis=1, inplace=True)
cols = list(data)
cols.insert(0, cols.pop(cols.index('lastname')))
data = data.ix[:, cols]
dictdata = data.set_index('lastname').T.to_dict('list')

first3pairs = {k: dictdata[k] for k in dictdata.keys()[:3]}

"""
first3pairs
{'Putt': [' PhD ScD', 'Professor of Biostatistics', 'mputt@mail.med.upenn.edu', ['Mary', 'E.', 'Putt']], 'Feng': [' Ph.D', 'Assistant Professor of Biostatistics', 'ruifeng@upenn.edu', ['Rui', 'Feng']], 'Bilker': ['Ph.D.', 'Professor of Biostatistics', 'warren@upenn.edu', ['Warren', 'B.', 'Bilker']]}
"""



###Second Dict

import pandas as pd
data = pd.read_csv('faculty.csv')
data['splitname'] = data['name'].str.split(' ')

data['tuple'] = [tuple(i) for i in data['splitname']]

data.drop(data.columns[[0]], axis=1, inplace=True)
data.drop(data.columns[[3]], axis=1, inplace=True)
dictdata = data.set_index('tuple').T.to_dict('list')

first3pairs = {k: dictdata[k] for k in dictdata.keys()[:3]}

"""
first3pairs
{('Hongzhe', 'Li'): [' Ph.D', 'Professor of Biostatistics', 'hongzhe@upenn.edu'], ('Jonas', 'H.', 'Ellenberg'): [' Ph.D.', 'Professor of Biostatistics', 'jellenbe@mail.med.upenn.edu'], ('Yimei', 'Li'): [' Ph.D.', 'Assistant Professor of Biostatistics', 'liy3@email.chop.edu']}
"""

###Still need to learn how to assign multiple values to unique keys in first dict, and how to sort by last name on the last list. In addition - might want to clean up names, titles and degrees?
