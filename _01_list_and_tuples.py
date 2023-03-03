def last(p) :
        return p[-1]

def sort(tuple):
        return sorted(tuple, key = last)

b = [(2, 5),(1, 2),(4,4),(2,3),(2,1)]
print('sorted : ')
print(sort(b))