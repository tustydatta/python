a = 5
b = "John"
print(a)
print(b)

c = 4
c = "Sally"
print(c)

# Casting 
d = str(3)
e = int(3)
f = float(3)
print(d)
print(e)
print(f)

g = 5
h = "John"
print(type(g))
print(type(h))

i = "John"
print(i)
j = 'John' #double quotes are the same as single quotes
print(j)

k = 4
K = "Sally"
print(k)
print(K)

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

l, m, n = "Orange", "Banana", "Cherry"
print(l)
print(m)
print(n)

o = p = q = "Orange"
print(o)
print(p)
print(q)

fruits = ["apple", "banana", "cherry"]
r, s, t = fruits
print(r)
print(s)
print(t)

u = "Python"
v = "is"
w = "awesome"
print(u, v, w)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

a = 5
b = 10
print(a + b)

c = 5
d = "John"
print(c, d)

# global variables
x = "awesome"
def myfunc():
    print("Python is " + x)
    print("Python is" , x)
myfunc()

a = "awesome"
def fun():
    a = "fantastic"
    print("Python is " + a)
fun()
print("Python is " + a)

def myfun():
    global x
    x = "fantastic"
myfun()
print("Pyhton is " + x)

a = "awesome"
def fun2():
    global a 
    a = "fantastic"
fun2()
print("Python is " + a)