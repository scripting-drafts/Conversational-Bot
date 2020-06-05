import pandas as pd
import csv
import itertools
from  graphviz import Digraph as d
from sys import argv
import itertools

file = argv[1]
df = pd.read_csv(file, delimiter='\t')
subreddits = list(dict.fromkeys(df.loc[:, 'sub']))
titles = list(dict.fromkeys(df.loc[:, 'title']))
dots = (title for title in titles)
childs_list = {}
parents_list = []

for parent in df['parent_id']:
	parents_list.append(parent)

parents = pd.Series(parents_list)

for sub in subreddits:

	for title, dot in zip(titles, dots):
		dot = d(comment=str(sub), engine='circo')

		for row in range(df.loc[df['title'] == title].index[0], df.loc[df['title'] == title].index[-1]+1):
			dot.node(str(df.loc[row,'id']), str(df.loc[row,'author']), shape='circle', fontname='helvetica')#, fixedsize='true', width='2', height='2')# + '\n' + str(df.loc[row, 'body']).replace('\s\s', '\n'))
			child = df.loc[row, 'id']

			try:
				related = parents.str.contains(child, case=True)
			except Exception as e:
				print(e)
				pass
			else:
				true_parents = df.loc[related, 'id']
				for parent in true_parents:
					dot.edge(child, parent, constraint = 'true')

			if df.loc[row, 'parent_id'] == 'main_parent':
				try:
					for children in df.loc[df['title'] == title, 'id']:
						dot.edge(str(df.loc[row, 'id']) + children)
				except Exception as x:
					print(x)

		dot.render('test-output/' + str(sub) + '-' + str(title).replace('/', ' ') + '.gv', view=True)
