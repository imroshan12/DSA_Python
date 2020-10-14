# Write a Python function frequency(l) that takes as input a list of integers and
# returns a pair of the form (minfreqlist,maxfreqlist) where:

# 1. minfreqlist is a list of numbers with minimum frequency in l, sorted in ascending order
# 2. maxfreqlist is a list of numbers with maximum frequency in l, sorted in ascending order

def frequency(l):
    s = set(l)
    s = list(s)
    s.sort()
    freqList = []
    minList = []
    maxList = []
    for i in range(len(s)):
        freqList.append(l.count(s[i]))
    minM = min(freqList)
    maxM = max(freqList)
    # print(freqList)
    # print(minM, maxM)
    # print(s)
    for i in range(len(s)):
        if l.count(s[i]) == minM and l.count(s[i]) == maxM:
            minList.append(s[i])
            maxList.append(s[i])
        elif l.count(s[i]) == minM:
            minList.append(s[i])
        elif l.count(s[i]) == maxM:
            maxList.append(s[i])
    minList.sort()
    maxList.sort()
    return (minList,maxList)