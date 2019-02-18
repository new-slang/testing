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

#    idx = []
#    mem = x[0]
#    for i in range(len(x)):
#        # `i` is a local maximum if the signal decreases before and after it
#        if x[i] > mem:
#            mem = x[i]
#    idx.append(mem)
#    return idx


if __name__ == "__main__":
    print('First Test')
    x = [0, 1, 2, 1, 2, 1, 0]
    print(x)
    print(find_maxima(x))
    x = [-i**2 for i in range(-3, 4)]
    print(x)
    print(find_maxima(x))
    x = [np.sin(2*alpha) for alpha in np.linspace(0.0, 5.0, 100)]
    #print(x)
    print('Long Array')
    print(find_maxima(x))
    
    
    print('Second Test')
    x = [4, 2, 1, 3, 1, 2]
    print(x)
    print(find_maxima(x))
    x = [4, 2, 1, 3, 1, 5]
    print(x)
    print(find_maxima(x))
    x = [4, 2, 1, 3, 1]
    print(x)
    print(find_maxima(x))
    
    print('Third Test')
    x = [1, 2, 2, 1]
    print(x)
    print(find_maxima(x))
    
    
    print('Fourth Test')
    x = [1, 2, 2, 3, 1]
    print(x)
    print(find_maxima(x))
    x = [1, 3, 2, 2, 1]
    print(x)
    print(find_maxima(x))
    x = [3, 2, 2, 3]
    print(x)
    print(find_maxima(x))