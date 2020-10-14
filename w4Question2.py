# An airline has assigned each city that it serves a unique numeric code. It has
# collected information about all the direct flights it operates, represented as
# a list of pairs of the form (i,j), where i is the code of the starting city and j
# is the code of the destination.
# It now wants to compute all pairs of cities connected by one intermediate hope — city i
# is connected to city j by one intermediate hop if there are direct flights of the form
# (i,k) and (k,j) for some other city k. The airline is only interested in one hop
# flights between different cities — pairs of the form (i,i) are not useful.
# Write a Python function onehop(l) that takes as input a list of pairs representing
# direct flights, as described above, and returns a list of all pairs (i,j), where i != j,
# such that i and j are connected by one hop. Note that it may already be the case that there
# is a direct flight from i to j. So long as there is an intermediate k with a flight from
# i to k and from k to j, the list returned by the function should include (i,j).
# The input list may be in any order. The pairs in the output list should be in
# lexicographic (dictionary) order. Each pair should be listed exactly once.
def onehop(codes):
    cities = []
    for (i, k1) in codes:
        for (k2, j) in codes:
            if k1 == k2 and i != j:
                cities.append((i,j))
    cities = set(cities)
    cities = list(cities)
    cities.sort()
    return cities