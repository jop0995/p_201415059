class Dog(object):
    def __init__(self,name):
        self.name=name
    def getName(self):
        print "my dog name is", self.name
    def talk(self):
        print "{0} sounds like mung mung...".format(self.name)
        
class ShihTzudog(object):
    def __init__(self,name):
        self.name=name     
    def talk(self):
        print "{0} sounds like si si ...".format(self.name)
  
class Maltese(object):
    def __init__(self,name):
        self.name=name     
    def talk(self):
        print "{0} sounds like mal mal ...".format(self.name)
  
        
m=Dog('puppy')
m.talk()
m1=ShihTzudog('sichu')
m1.talk()
m2=Maltese('maltis')
m2.talk()