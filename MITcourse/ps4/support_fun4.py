s = 'abc'

# result = []
# for x in L:
#     for j in range(len(x)+1):
#         result.append(x[:j] + s[0] + x[j:])

# print(result)
# print(L[0:])

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    n = len(sequence)
    result = []
    if n == 1:
        result.append(sequence)
        return result
    else:
        result = []
        for x in get_permutations(sequence[1:]):
            for j in range(len(x)+1):
                result.append(x[:j] + sequence[0] + x[j:])
        return result

# print(get_permutations(s))
def fac(n):
    result = 1
    for i in range(1,n):
        result = result * i
    return result*n

n = len(s)
L = list(s)
result = []
for i in range(fac(n)):
    a = []
    a.append(L[i % 3])
    a.append(L[(i+1) % 3])
    a.append(L[(i+2) % 3])
    result.append(''.join(a))

print(result)