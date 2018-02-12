sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']



#integer
isinstance(<mI>,int)
if mI >=100 
     print "thats a big number"
else:
    print 'thats a small number'

#String
if len(bS>=50:
    print "long sentence."
    else:
        print "short sentence."

#List
if isinstance(lL,list):
    if len(lL) >=10:
        print "big list"
    else:
        print "short"








#multiples
for x in range(1, 1000):
    if(x % 2 == 1):
        print x

for x in range(5, 1000001):
    if(x % 5 ==0):
        print x

#sum List
a = [1, 2, 5, 10, 255, 3]
b = sum(a)
print b

a = [1,2,5,10,255,3]
sum = 0

avg = sum/len(a)
for num in a:
    sum += num

print avg

for i in range(1,2001):
    if i % 2 == 0:
        print 'Number is ' + str(i) + '. This is an odd number.'
    else:
        print 'Number is ' + str(i) + '. This is an even number.'

a = [2,4,10,16]
def multiply(arr):
    for i in range(len(arr)):
        arr[i] = arr[i] * 5
    return arr

b = multiply(a)
print b


