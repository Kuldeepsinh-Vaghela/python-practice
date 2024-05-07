## MULTILEVEL INHERITANCE
class Grandpa:
    def __init__(self,name,age,wife,grandkids):
        self.name = name
        self.age = age
        self.wife = wife
        self.grandkids = grandkids
    
    def displayInfo(self):
        print(f"My name is {self.name}\n"
              f"My age is {self.age}\n"
              f"My wife's name is {self.wife}\n"
              f"I have {self.grandkids} grandkids")


class Father(Grandpa):
    def __init__(self,name,age,wife,kids):
        super().__init__(name,age,wife,"0")
        self.kids = kids
    
    def displayInfo(self):
        print(f"My name is {self.name}\n"
              f"My age is {self.age}\n"
              f"My wife's name is {self.wife}\n"
              f"I have {self.kids} kids")


class Son(Father):
    def __init__(self,name,age):
        super().__init__(name,age,"No one","0")
        
    
    def displayInfo(self):
        print(f"My name is {self.name}\n"
              f"My age is {self.age}\n")
        

grdpa = Grandpa("aman",63,"sura",3)
print("Grandpa Info: \n")
grdpa.displayInfo()

pa = Father("suresh",35,"mura",3)
print("Father Info: \n")
pa.displayInfo()

sn = Son("deep",12)
print("Son Info: \n")
sn = Son("deep",12)
sn.displayInfo()

#######################################################################

## MULTIPLE INHERITANCE

class Study:
    def studyInfo(self):
        print("Subject name: Maths")
        print("Subject score is : 100")


class Games:
    def gameInfo(self):
        print("Game name is : Cricket")

class Person(Study,Games):
    pass
        
a = Person()
a.studyInfo()
a.gameInfo()

###########################################################################

## SINGLE INHERITANCE

class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

    def make_sound(self):
        print(f"The {self.species} makes a sound: {self.sound}")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__("Dog", "Bark")
        self.name = name
        self.breed = breed

    def display_info(self):
        print(f"Name: {self.name}\nSpecies: {self.species}\nBreed: {self.breed}")


dog = Dog("tommy","german shepherd")
dog.display_info()
dog.make_sound()