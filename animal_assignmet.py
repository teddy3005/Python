class Animal(object):
    def __init__(self,name):
        self.name=name
        self.health=100

    def walk(self):
        self.health-=1
        return self
    def run(self):
        self.health-=5
        return self
    def displayHealth(self):
        print "health",self.health

class Dog(Animal):
    def __init__(self,name):
        super(Dog,self).__init__(name)
        self.health=150
    def pet(self):
        self.health += 5
        return self  

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def displayHealth(self):
        print "This is a dragon"
        super(Dragon, self).displayHealth()


animal_1 = Animal('teddy')
animal_1.walk().walk().walk().run().run().displayHealth()

dragon1=Dragon("fluffy")
dragon1.fly().fly().displayHealth()

#animal1.run().displayHealth()