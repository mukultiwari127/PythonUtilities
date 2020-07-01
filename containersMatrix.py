# David has several containers, each with a number of balls in it. 
# He has just enough containers to sort each type of ball he has into its own container. 
# David wants to sort the balls using his sort method.

# As an example, David has  containers and  different types of balls, 
# both of which are numbered from  to . The distribution of ball types per container 
# are described by an  matrix of integers, .


import math
import os
import random
import re
import sys
import collections

def organizingContainers(container):
    flag = False
    type_element = {}
    container_element = {}
    for j in range(len(container)):
        sumj = 0
        sumi = 0
        for i in range(len(container)):
            sumj = sumj + container[i][j]
            sumi = sumi + container[j][i]
        type_element[j] = sumj
        container_element[j] = sumi

    type_element = sorted(type_element.items(), key=lambda kv: kv[1])
    container_element = sorted(container_element.items(), key=lambda kv: kv[1])

    for i in range(len(type_element)):
        if type_element[i][1] != container_element[i][1]:
            flag = True

    if flag:
        return("Impossible")
    else:
        return("Possible")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()