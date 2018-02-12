l = ['magical unicorns',19,'hello',98.98,'world']
newstr=[]
newNum=[]
for i in l:
    if type (i)==str: 
        newstr.append(i)
    elif type (i)==int:
        newNum.append(i)
    elif type (i)==float:
        newNum.append(i)
    else:
        print "not valid"
print newstr
print sum(newNum)


        
        
