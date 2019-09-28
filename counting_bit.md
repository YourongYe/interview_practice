# Two methods
```py
def count_bits(x):
    num_bit = 0
    while x:
        num_bit += 1
        x = x & x-1
        print(x)
    return num_bit


def count_bits1(x):
    num_bit = 0
    while x:
        num_bit += x&1
        x >>= 1
        print(x)
    return num_bit

print(count_bits(2000))
print('lll')
print(count_bits1(200))
```

#Result
```py
1984
1920
1792
1536
1024
0
6
lll
100
50
25
12
6
3
1
0
3
```
