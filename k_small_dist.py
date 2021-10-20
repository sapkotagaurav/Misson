import time
import math


def calculate_small(points):
    result =[]
    lowest=[]   
    distance = (points[0][0] -points[1][0] )**2+ (points[0][1] - points[1][1])**2

    for a in range(0,len(points)):
        for b in range(a+1, len(points)):
            dist = (points[a][0] -points[b][0] )**2+ (points[a][1] - points[b][1])**2
            result.append((dist**0.5,(points[a],points[b])))
            if dist<distance:
                distance = dist
                lowest = [points[a],points[b]]
    print(result)
    return (lowest,distance**0.5)


def take_input():
    lists = []
    print("Type anything except number to submit")
    while True:
        try:
            x = float(input("Enter x of the point:\t"))
            y = float(input("Enter y of the point:\t"))
            lists.append((x,y))
        except ValueError:
            print("Done...")
            break
    print("Fro here",lists)
    return lists

print(calculate_small(take_input()))



