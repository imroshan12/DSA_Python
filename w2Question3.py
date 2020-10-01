# Write a function shuffle(l1,l2) that takes as input two lists, 11 and l2, and returns a list consisting
# of the first elment in l1, then the first element in l1, then the second element in l2, then the
# second element in l2, and so on. If the two lists are not of equal length, the remaining elements of
# the longer list are appended at the end of the shuffled output.
# Here are some examples to show how your function should work.


def shuffle(l1,l2):
    i,j = 0,0
    a = min(len(l1),len(l2))
    finalList = []
    while i < a and j < a:
        finalList.append(l1[i])
        i += 1
        finalList.append(l2[j])
        j += 1
    if max(len(l1),len(l2)) > a:
        if len(l1) > len(l2):
            finalList += l1[a:]
        else:
            finalList += l2[a:]
    return finalList
shuffle([0,1],[4,5,6])





# def shuffle(l1,l2):
#     a = min(len(l1),len(l2))
#     finalList = []
#     for i in range(2*a):
#         if i%4 == 0:
#             finalList.append(l1[i//2])
#         elif (i+1)%4 == 0:
#             finalList.append(l1[(i-1)//2])
#         elif (i-1)%4 == 0:
#             finalList.append(l2[(i - 1)//2])
#         elif (i - 2)%4 == 0:
#             finalList.append(l2[i//2])
#     if max(len(l1),len(l2)) > a:
#         if len(l1) > len(l2):
#             finalList += l1[a:]
#         else:
#             finalList += l2[a:]
#     return finalList