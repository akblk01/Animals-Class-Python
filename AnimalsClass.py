import time
class Animals():

    def __init__(self, Name= "", Feature="", NumOfFeet=""):
        self.NumOfFeet = NumOfFeet
        self.Feature = Feature
        self.Name = Name

    def addAnimal(self):
        self.Name = addAnimalName
        self.Feature = addAnimalFeature
        self.NumOfFeet = addAnimalNumOfFeet

    def __str__(self):
        return "Animal Name: {}\nAnimal Feature: {}\nAnimal Number Of Feet: {}".format(self.Name,self.Feature,self.NumOfFeet)


class Dogs(Animals):
    def __init__(self, Name, Feature, NumOfFeet, Size):
        super().__init__(Name, Feature, NumOfFeet)
        self.Size = Size

    def __str__(self):
        return "Animal Name: {}\nAnimal Feature: {}\nAnimal Number Of Feet: {}\nAnimal Size: {}".format(self.Name,self.Feature,self.NumOfFeet,self.Size)


class Birds(Animals):
    def __init__(self,Name,Feature,NumOfFeet,CanItFly):
        super().__init__(Name,Feature,NumOfFeet)
        self.CanItFly = CanItFly

    def __str__(self):
        return "Animal Name: {}\nAnimal Feature: {}\nAnimal Number Of Feet: {}\nAnimal Can It Fly: {}".format(self.Name,self.Feature,self.NumOfFeet,self.CanItFly)

class Horses(Animals):
    def __init__(self,Name,Feature,NumOfFeet,Type):
        super().__init__(Name,Feature,NumOfFeet)
        self.Type = Type

    def __str__(self):
        return "Animal Name: {}\nAnimal Feature: {}\nAnimal Number Of Feet: {}\nAnimal Type: {}".format(self.Name,self.Feature,self.NumOfFeet,self.Type)


animalOne = Animals()
animalTwo = Animals()
animalThree = Animals()
animalFour = Animals()
animalFive = Animals()


print("""
********************
Zoo Animal Tracking
********************

1- See All Animals
2- Add New Animal
3- Log out by pressing 'Q'
""")
while True:
    transaction_Number = input("Enter the transaction number :")
    if transaction_Number == "Q":
        print("Checking out...")
        time.sleep(1)
        break

    elif transaction_Number == "1":
        print(animalOne)

    elif transaction_Number == "2":
        addAnimalName = input("Animal Name :")
        addAnimalFeature = input("Animal Feature :")
        addAnimalNumOfFeet = input("Animal Number of Feet :")

        animalOne.addAnimal()

        print("Adding...")
        time.sleep(1)
        print("Added.")


