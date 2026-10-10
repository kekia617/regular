def main():
    L = [-12, -5, 0, 3, 7, 11, 14, 18, 22, 29, 35, 41, 50, 68, 88]
    J = ['A', 'C', 'F', 'H', 'K', 'M', 'P', 'R', 'T', 'V', 'W', 'X', 'Y', 'Z', 'a']
    print(search(J, 'M'))
     

def search(L, e):
    """Assumes L is a list, the elements of which are in 
    ascending order. 
    Returns True if e is in L and False otherwise"""
    def binary_search(L, e, low, high):
        if low == high:
            return L[low] == e
        
        mid = (low+high)//2

        if L[mid] == e:
            return True
        elif L[mid] > e:
            return binary_search(L, e, low, mid-1)
        else:
            return binary_search(L, e, mid + 1, high)
    if len(L) == 0:
        return False
    else:
        return binary_search(L, e, 0, len(L)-1)

main()