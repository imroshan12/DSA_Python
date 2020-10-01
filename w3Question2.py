# In a list of integers l, the neighbours of l[i] are l[i-1] and l[i+1]. l[i] is a
# hill if it is strictly greater than its neighbours and a valley if it is strictly
# less than its neighbours.
# Write a function counthv(l) that takes as input a list of integers l and returns a
# list [hc,vc] where hc is the number of hills in l and vc is the number of valleys in l.

def counthv(l):
    h_v = [0,0]
    for i in range(1,len(l) - 1):
        if l[i] > l[i-1] and l[i] > l[i+1]:
            h_v[0] += 1
        elif l[i] < l[i-1] and l[i] < l[i+1]:
            h_v[1] += 1
        else:
            pass
    return h_v