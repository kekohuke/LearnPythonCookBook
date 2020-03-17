p = (4, 5) # this () is called *sequence*
x, y = p # unpacking
print(x)
print(y)

# another example

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name)
print (date)

name, shares, price, (year, mon, day) = data

print(year)
print(mon)

s = 'New String' #unpacking work with any object that happens to be iterable, not jst tuple and lists
a, b, c, d, e, f, g, h, i, j = s 
print(a)
print(b)
print(c)
print(d)
print(f)

data = ['ACME', 50, 91.1, (2012,12,21)]
_, shares, price, _ = data #discard certain value
print(shares)
print(price)

