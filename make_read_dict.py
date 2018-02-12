#name='Anna'
#age=101
#country='The United States'
#language='English'

Diction={"name":"Anna", "age":101,"country":"The United States","Favorite language":"Python"}
me={"name":"Ted", "age":103,"country":"The United States","Favorite language":"Java"}

def functionName(stuff):
    for key, data in stuff.iteritems():
        if key=="name":
            print "My name is"+"", data
        if key=="age":
            print "My age is"+"", data
        if key=="country":
            print "My Country of birth is the"+"",data
        if key=="Favorite language":
            print "My favoriite language is"+"", data

functionName(Diction)




'''def myName(i,persons,age,country):
  for i in 
  print 'My name is '+persons[i]
  print 'My age is ' +age[i]
  print "My country of birth is The "+country[i]
  print 'My favorite language is '+language[i]'''







