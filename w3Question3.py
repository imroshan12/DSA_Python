# Write a function leftrotate(m) that takes a list representation m
# of a square matrix as input, and returns the matrix obtained by rotating the original
# matrix counterclockwize by 90 degrees

def leftrotate(m):
    a = len(m)
    l2 = []
    for j in range(a-1,-1,-1):
        l1 = []
        for i in range(a):
            l1.append(m[i][j])
        l2.append(l1)
    return l2