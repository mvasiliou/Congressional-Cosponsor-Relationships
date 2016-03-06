'''
{senator:{relationships:{senator:number}}}

for senator in rep_dict:
	

1. generate matrix
2. sqrt each cell (to flatten out matrix)
3. transition matrix?
'''

def normalize_matrix(some_matrix):
	# Based on https://github.com/govtrack/govtrack.us-web/blob/master/analysis/sponsorship_analysis.py
	# this is weird. idk if this is what i want it to do
	(rows, cols) = some_matrix.shape
	for i in range(cols):
		column = some_matrix[:,i]
		s = sum(column)
		some_matrix[:,i] = column/s
	return some_matrix




def transitions(sponsorship):
	out_degrees = []
	for i in sponsorship:
		out_degrees.append(sum(i))
	n = len(out_degrees)
	transition_matrix = (0.9*sponsorship/out_degrees) + (0.1*1/n)
	return transition_matrix

def markov_rank(transition_matrix, num_steps):
	return None