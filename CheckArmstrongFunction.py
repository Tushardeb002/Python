def order(m):
    count = 0
    while m != 0:
        m = m // 10
        count = count + 1
    return count
def num(n):
    sum = 0
    c = order(n)
    while n > 0:
        x = n % 10
        sum = sum + (x**c)
        n = n // 10
    return sum
y = int(input())
d = num(y)
if y == d:
    print('true')
else:
    print('false')
