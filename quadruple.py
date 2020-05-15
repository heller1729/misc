from itertools import combinations
def quad(l, x):
    def valid(tup):
        return sum(tup) == x
    return list(filter(valid, list(combinations(l, 4))))
l = [0, -1, 2, 3, -2, 4, 5]
print(quad(l, 2))