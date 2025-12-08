import math
import sys
import bisect

def distance(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2+ (p1[2] - p2[2])**2

def insert(d, l):
    for i in range(len(l)):
        if l[i][1] > d:
            return i
    return -1

with open("test", "r") as file:
    lines = file.readlines()
    coords = [[int(v) for v in l.split(",")] for l in lines]
    l_coords = len(coords)
    min_dist = [(-1, sys.maxsize)] * 10
    m = [[0] * l_coords for _ in range(l_coords)]
    print("CreateMap")
    for i in range(l_coords - 1):
        for j in range(i + 1, l_coords):
            m[i][j] = distance(coords[i], coords[j])
            ins = insert(m[i][j], min_dist)
            if ins > -1:
                min_dist.insert(ins, ((i,j), m[i][j]))

    clusters = []
    print("GetClusters")
    for i in range(10):
        actual_coords = min_dist[i][0]
        ci = 0
        while ci < len(clusters):
            c = clusters[ci]
            if actual_coords[0] in c:
                c.add(actual_coords[1])
                break
            elif actual_coords[1] in c:
                c.add(actual_coords[0])
                break
            ci += 1
        if ci == len(clusters):
            clusters.append(set([actual_coords[0], actual_coords[1]]))

    changes = True
    while changes:
        for i in range(len(clusters)):
            for i2 in range(len(clusters)):
                if clusters[i].union(clusters[i2]) is not None:
                    clusters[i]

    print(clusters)

    print(len(clusters[0]) * len(clusters[1]) * len(clusters[2]))

