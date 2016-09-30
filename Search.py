# File:			Search.py
# Author: 		Luke Privett
# Date: 		02/09/2016
# Course:		CMSC 471
# E-mail:		privett1@umbc.edu
# Description:  hill climb, hill climb with restarts, and simulated annealing
# Run by: python Search.py <input file> <output file> <start node> <end node> <search_type>
# References:
#
#
#
#  --------------------------------------------------------------------------

import math
import time
# import plotly.plotly as py
# import plotly.graph_objs as go

def my_function(x, y):
    r = math.sqrt(x**2 + y**2)
    # z = (sin(x^2+3y^2)/(0.1+r^2))+(x^2+5y^2)*(exp(1-r^2)/2), r=sqrt(x^2+y^2)
    z = (math.sin(x**2 + 3*y**2)/(0.1 + r**2))
    return z


# hill_climb(function_to_optimize, step_size, xmin, xmax, ymin, ymax)
def hill_climb(function, step_size, x_min, x_max, y_min, y_max):
    # initialize to origin
    x = 0
    y = 0
    # set step size
    step = step_size
    # check initial value
    current = eval(function)(x, y)

    # check possibilities
    pos1 = eval(function)(x - step, y + step)  # up and left
    pos2 = eval(function)(x, y + step)  # up
    pos3 = eval(function)(x, y + step)  # up and right
    pos4 = eval(function)(x - step, y)  # left
    pos5 = eval(function)(x, y)  # right
    pos6 = eval(function)(x - step, y - step)  # down and left
    pos7 = eval(function)(x, y - step)
    pos8 = eval(function)(x + step, y - step)

    if current > pos1 and current > pos2 and current > pos3 and current > pos4 and current > pos5 and current > pos6 and current > pos7 and current > pos8:
        return current  # end search if no neighbors are higher

    # otherwise pick a random one to move towards

    # loop until there is not a higher

    while x_min <= x <= x_max and y_min <= y <= y_max:  # try possibilities within range
        break
    else:
        print("Peak left range")
        return current

    return current


# hill_climb_random_restart(function_to_optimize, step_size, num_restarts, x_min, x_max, y_min, y_max)
def hill_climb_random_restart(function, step_size, num_restarts, x_min, x_max, y_min, y_max):
    pass


# simulated_annealing(function_to_optimize, step_size, max_temp, x_min, x_max, y_min, y_max)
def simulated_annealing(function, step_size, max_temp, x_min, x_max, y_min, y_max):
    pass


def search(selection):
    if selection == 1:
        return hill_climb("my_function", .1, -2.5, 2.5, -2.5, 2.5)
    elif selection == 2:
        return hill_climb_random_restart("my_function", .1, 5, -2.5, 2.5, -2.5, 2.5)
    elif selection == 3:
        return simulated_annealing("my_function", .1, 100, -2.5, 2.5, -2.5, 2.5)
    elif selection == 4:
        # search with all 3
        pass
    else:
        return 0
    pass


def main():
    start_time = time.time()
    # basic execution
    # call the function
    print(search(1))

    print ("End")
    print ("Time taken: " + str(time.time() - start_time) + ' s')

main()