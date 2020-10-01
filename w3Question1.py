# Write a function contracting(l) that takes as input a list of integer l and returns
# True if the absolute difference between each adjacent pair of elements strictly decreases.

def contracting(l):
    previousDifference = abs(l[1] - l[0])
    for i in range(1,len(l) - 1):
        currentDifference = abs(l[i+1] - l[i])
        if currentDifference >= previousDifference:
            return False
        previousDifference = currentDifference
    return True