import random as rd
import numpy as np
import itertools
rd.seed(10)

default_parameters = {
    'C' : 0.5,
	'D' : 40,
	'M' : 35,
	'F' : 20,
	'R' : 0,
}

def make_matrix(size : int = 10):
    param = default_parameters
    forest = np.zeros((size,size),dtype=str)
    for i,j in itertools.product(range(size),range(size)):
        forest[i,j] = rd.choices(
            list(param.keys()),
            weights=list(param.values()),
            k=1
        )[0]
    return forest

def stats_forest(forest, p : bool = False):
    unique, count = np.unique(forest,return_counts=True)
    stats = dict(zip(unique,count))
    if p : print(stats)
    return stats

if __name__ == "__main__":
    forest = make_matrix()
    print(forest)
    print()
    print('Calcul')
    stats_forest(forest)

    #Test sur 30 forest
    general_stats = {'C':0, 'D':0, 'M':0, 'F':0, 'R':0}
    nbr_forest=1000
    for i in range(nbr_forest):
        forest = make_matrix(10)
        stat = stats_forest(forest)
        for key,value in stat.items():
            general_stats[key]+=value
    for key,value in general_stats.items():
        general_stats[key] = general_stats[key]/nbr_forest
    print(general_stats)