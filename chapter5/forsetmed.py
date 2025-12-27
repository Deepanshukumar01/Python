a={2,4,5,6,7,8,23,45}
b={4,6,99}

c=a.union({4,6})
print(c)

print(a.union(b))
print(a.intersection(b))

d=a-b
print(d)