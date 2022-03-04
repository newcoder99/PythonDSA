import math
def euclideanDistance(coordinate1, coordinate2):
    return pow(pow(coordinate1[0] - coordinate2[0], 2) + pow(coordinate1[1] - coordinate2[1], 2), .5)
                     
def minDistance(P):
    n=len(P)
    min_val = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            if euclideanDistance(P[i], P[j]) < min_val:
                min_val = euclideanDistance(P[i], P[j])
 
    return round(min_val,2)
    
pts = eval(input())
timeout = 3.0  # Time