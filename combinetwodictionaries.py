d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3 = {k: d1.get(k, 0) + d2.get(k, 0) for k in set(d1) | set(d2)}
print(d3)