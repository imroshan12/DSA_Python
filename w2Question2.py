# Write a function delchar(s,c) that takes as input strings s and c, where c has length 1
# (i.e., a single character), and returns the string obtained by deleting all occurrences of c in
# s. If c has length other than 1, the function should return s
# Here are some examples to show how your function should work.
def delchar(s,c):
    if len(c) != 1:
        return s
    else:
        return s.replace(c,"")