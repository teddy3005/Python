'''greeting='hello'
name='dojo'
print name + greeting

lists=['Wish', 'Mop', 'Bleet', 'March', 'Jerk'] 
for i in range(len(lists)):
    print lists[i]

def multiply(num):
    lists=[]
    for i in range(0,26):
        num=num*2
        lists.append(num)
    print lists
multiply(2)

def reverse(txt):
    char=[]
    l=len(txt)
    last= l-1
    for i in range (l):
        char.append(txt[last])
        last-=1

    result=""
    for j in char:
        result +=j
    return result 
print reverse('hello') 

x=10
x*=7
y=30
z=y+x
z=z*3
z=z-y
z=z/27
x=z+y
y=3
x=x+y

if (x%10==0):
    print True
else:
    print False





