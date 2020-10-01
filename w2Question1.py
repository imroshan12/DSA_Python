# A positive integer m is a prime product if it can be written as p×q, where p and q are both
# primes.
# Write a Python function primeproduct(m) that takes an integer m as input and returns
# True if m is a prime product and False otherwise. (If m is not positive, your function
# should return False.)
def primeproduct(m):
    primeList = []
    if m < 0:
        return False
    if m==1 or m==2:
        return True
    for i in range(1,m//2+1):
        prime = True
        for j in range(1,i//2+1):
            if j != 1 and i % j == 0:
                prime = False
                break
        if prime:
            primeList.append(i)
    for i in primeList:
        x = m//i
        if (x in primeList) and (x*i == m):
            return True
    return False
print(primeproduct(2))