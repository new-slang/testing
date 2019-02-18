import numpy as np

def find_maxima(x):
    """Find local maxima of x.

    Example:
    >>> x = [1, 2, 3, 2, 4, 3]
    >>> find_maxima(x)
    [2, 4]

    Input arguments:
        x -- 1D list numbers

    Output:
        idx -- list of indices of the local maxima in x
    """
    idx = []
    for i in range(len(x)):
        check = True
        # `i` is a local maximum if the signal decreases before and after it
        if not i==0 and not i==len(x)-1:
            if x[i-1] < x[i] and x[i+1] < x[i]:
                idx.append(i)
                check = False
            if check and x[i]==x[i+1]:
                j=2
                while x[i]==x[i+j]:
                    j += 1
                if x[i] > x[i+j] and x[i-1] < x[i]:
                    for c in range(j):
                        idx.append(i+c)
                        check = False
        if i==0 and check and x[i+1] < x[i]:
            idx.append(i)
            check = False
        if i==len(x)-1 and check and x[i-1] < x[i]:
            idx.append(i)
            check = False
    return idx