############################################################################

# Created by: Prof. Valdecy Pereira, D.Sc.
# UFF - Universidade Federal Fluminense (Brazil)
# email:  valdecy.pereira@gmail.com
# Course: Metaheuristics
# Lesson: Local Search-2-opt

# Citation: 
# PEREIRA, V. (2018). Project: Metaheuristic-Local_Search-2-opt, File: Python-MH-Local Search-2-opt.py, GitHub repository: <https://github.com/Valdecy/Metaheuristic-Local_Search-2-opt>

############################################################################

# Required Libraries
import pandas as pd
import copy

# Function: 2_opt
def local_search_2_opt(Xdata, city_tour, full_swap = True, recursive_seeding = 1):
    count = 0
    city_list = copy.deepcopy(city_tour)
    while (count < recursive_seeding):
        distance = 0
        best_route = copy.deepcopy(city_list)
        seed = copy.deepcopy(city_list)        
        for i in range(0, len(city_list[0]) - 2):
            for j in range(i, len(city_list[0]) - 1):
                opt_1 = int(i)
                opt_2 = int(j)           
                value_opt_1 = copy.deepcopy(seed[0][opt_1])
                value_opt_2 = copy.deepcopy(seed[0][opt_2])           
                if (full_swap == False):
                    best_route[0][opt_1] = value_opt_2
                    best_route[0][opt_2] = value_opt_1    
                elif (full_swap == True):
                    best_route[0][opt_1:opt_2+1] = list(reversed(best_route[0][opt_1:opt_2+1]))           
                best_route[0][-1]  = best_route[0][0]              
                for k in range(0, len(city_list[0])-1):
                    m = k + 1
                    distance = distance + Xdata.iloc[best_route[0][k]-1, best_route[0][m]-1]            
                best_route[1] = distance           
                if (distance < city_list[1]):
                    city_list[1] = copy.deepcopy(best_route[1])
                    for n in range(0, len(city_list[0])): 
                        city_list[0][n] = best_route[0][n]          
                best_route = copy.deepcopy(seed)
                distance = 0
        count = count + 1  
        print(city_list)
    return city_list

######################## Part 1 - Usage ####################################

X = pd.read_csv('Python-MH-Local Search-2-opt-Dataset-01.txt', sep = '\t') #17 cities => Optimum = 2085

cities = [[   1,  2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,   1   ], 4722]
ls2opt = local_search_2_opt(X, city_tour = cities, full_swap = True, recursive_seeding = 11)
