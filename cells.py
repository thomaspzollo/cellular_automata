
import numpy as np
import random

from PIL import Image
import matplotlib
import matplotlib.pyplot as plt



pop_size = 24
num_gens = 100

def generateWithRule(gen, rule):

	next_gen = []
	for idx, cell in np.ndenumerate(gen):
		idx = idx[0]
		if idx == 0:
			if gen[1] == 1:
				next_gen.append(rule[0])
			else:
				next_gen.append(rule[1])
		elif idx == (pop_size - 1):
			if gen[(pop_size - 2)] == 1:
				next_gen.append(1)
			else:
				next_gen.append(0)
		else:
			n1 = gen[idx-1]
			n2 = gen[idx+1]
			if (n1 == 1 and n2 == 0) or (n1 == 0 and n2 == 1):
				next_gen.append(1)
			else:
				next_gen.append(0)
	return next_gen

###############################################################
###############################################################

grid = np.zeros((num_gens,pop_size))

starting_pop = []
for i in range(pop_size):
	starting_pop.append(random.randint(0, 1))

starting_pop = np.array(starting_pop)
grid[0,:] = starting_pop

for p0 in range(2):
	for p1 in range(2):
		for p2 in range(2):
			for p3 in range(2):
				for p4 in range(2):
					for p5 in range(2):
						rule = [p0,p1,p2,p3,p4,p5]
						for i in range(num_gens-1):
							next_gen = np.array( generateWithRule(grid[i,:], rule) )
							grid[i+1,:] = next_gen
						filename = "".join(map(str, rule)) + '_image.jpg'
						plt.imsave(filename, grid)




