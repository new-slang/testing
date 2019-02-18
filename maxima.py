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
        if len(x)==1:
            idx.append(i)
            check=False
        if len(x)==2 and check and i==0:
            if x[i+1] == x[i]:
                idx.append(i)
                idx.append(i+1)
                check=False
        if not i==0 and not i==len(x)-1 and check:
            if x[i-1] < x[i] and x[i+1] < x[i]:
                idx.append(i)
                check = False
        if not i==len(x)-1 and check:
            if check and x[i]==x[i+1]:
                j=1
                while x[i]==x[i+j] and i+j<len(x)-1:
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

    if idx == []:
        idx.append(len(x)-1)
        for i in range(len(x)-1):
            if x[len(x)-1-i] == x[len(x)-2-i]:
                idx.insert(0,len(x)-2-i)
    return idx

def test_one():
    x = [0, 1, 2, 1, 2, 1, 0]
    assert find_maxima(x) == [2, 4]

    x = [-i**2 for i in range(-3, 4)]
    assert find_maxima(x) == [3]

    x = [np.sin(2*alpha) for alpha in np.linspace(0.0, 5.0, 100)]
    assert find_maxima(x) == [16, 78]

def test_boundaries():
    x = [4, 2, 1, 3, 1, 2]
    assert find_maxima(x) == [0, 3, 5]

    x = [4, 2, 1, 3, 1, 5]
    assert find_maxima(x) == [0, 3, 5]

    x = [4, 2, 1, 3, 1]
    assert find_maxima(x) == [0, 3]

def test_saddle():
    x = [1, 2, 2, 1]
    assert find_maxima(x) == [1, 2]

def test_four():
    x = [1, 2, 2, 3, 1]
    assert find_maxima(x) == [3]

    x = [1, 3, 2, 2, 1]
    assert find_maxima(x) == [1]

    x = [3, 2, 2, 3]
    assert find_maxima(x) == [0, 3]

def test_five():
    x = [1, 2]
    assert find_maxima(x) == [1]

    x = [2, 1]
    assert find_maxima(x) == [0]

    x = [1, 1]
    assert find_maxima(x) == [0, 1]

def test_six():
    x = [4]
    assert find_maxima(x) == [0]

def test_seven():
    x = [1, 3, 2]
    assert find_maxima(x) == [1]
    
    x = [3, 3, 1]
    assert find_maxima(x) == [0, 1]
    
    x = [1, 3, 3]
    assert find_maxima(x) == [1, 2]
    
    x = [3, 3, 3]
    assert find_maxima(x) == [0, 1, 2]


if __name__ == "__main__":
    test_seven()
    
    print('Done')
