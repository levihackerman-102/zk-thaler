from math import sqrt
from functools import reduce

def chi_step(w, x):
    return x*w + (1-x)*(1-w)

def i_to_idx(i, n):
    x = [c == '1' for c in format(i, f'0{n}b')]
    return x

def chi_w(w, r):
    assert(len(w) == len(r))
    return reduce(lambda acc, pair: acc * chi_step(*pair), zip(w, r), 1)
    
def naive_mle(fw, r, p):
    assert(len(r) == sqrt(len(fw)))
    return sum(val * chi_w(i_to_idx(i, len(r)), r) for i, val in enumerate(fw)) % p
    
if __name__ == '__main__':
    assert(naive_mle([1,2,1,4],[0,2],5) == 3)
    
