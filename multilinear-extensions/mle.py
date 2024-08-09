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

def recurse(fw, r, n):
    if n == 0:
        return 0
    else:
        return recurse(fw, r, n-1) + fw[n-1] * chi_w(i_to_idx(n-1, len(r)), r)
    
def stream_mle(fw, r, p):
    return recurse(fw, r, 2**len(r)) % p

def memoize(r, v):
    if v == 1:
        return [chi_step(False, r[v-1]), chi_step(True, r[v-1])]
    else:
        previous_memo = memoize(r, v-1)
        result = []
        for val in previous_memo:
            result.append(val * chi_step(False, r[v-1]))
            result.append(val * chi_step(True, r[v-1]))
        return result

def dynamic_mle(fw, r, p):
    chi_lookup = memoize(r, len(r))
    # print(chi_lookup)
    return sum(left * right for left, right in zip(fw, chi_lookup)) % p
    
if __name__ == '__main__':
    assert(naive_mle([1,2,1,4],[0,2],5) == 3)
    assert(stream_mle([1,2,1,4],[0,2],5) == 3)    
    assert(dynamic_mle([1,2,1,4],[0,2],5) == 3)    
    