list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5]

print cmp(list_one,list_two)
if cmp(list_one,list_two) ==0:
    print "identical"
else:
    print"not the same"