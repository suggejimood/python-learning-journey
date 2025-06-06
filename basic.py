x = 42 #int
y = 3.14 #float
z = True #bool
c = 2 + 3j #complex
s = "Mehmet TAN" #str
b = b'abc' #bytes
ba = bytearray(b'abc') #bytearray
l = [1,2,3] #list
t = (1,2,3) #tuple
s = {1,2,3} #set
fs = frozenset([1,2,3]) #frozenset
d = {"a": 1, "b": 2} #dict

print("x: " + str(type(x)) + " y: " + str(type(y)) + " z: " + str(type(z)) + " c: " + str(type(c)) + " s: " + str(type(s)) + " b: " + str(type(b)) + " ba: " + str(type(ba)) + " l: " + str(type(l)) + " t: " + str(type(t)) + " s: " + str(type(s)) + " fs: " + str(type(fs)) + " d: " + str(type(d)) )

print(isinstance(x , int))
print(x.__class__.__name__)

numberCasting = int("42")
floatCasting = float("3.45")
stringCasting = str(123)
boolCasting = bool([])

a = 5
b = a

print(str(id(a)) + " " +str(id(b))) #atama kopyalama değildir referans aktarımıdır.