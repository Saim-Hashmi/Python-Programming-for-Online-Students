#Question 5: Write a code in python in which create a class named it Car which have 5 attributes such like (model, color and name etc.) and 3 methods.
#And create 5 object instance from that class.

class Car:
    def __init__(self,model,color,name,cc,speakers):
        self.model = model
        self.color = color
        self.name = name
        self.cc = cc
        self.speakers = speakers

    def printDetails(self):
        print("Car Name : {}\nCar Color : {}\nCar Model : {}\nCC : {}\nSpeakers? : {}".format(self.name,self.color,self.model,self.cc,self.speakers))
        print("---------------------------------------------------------------------------")

    def updateSpeakers(self,updatedData):
        self.speakers = updatedData

    def updateColor(self,updatedColorData):
        self.color = updatedColorData

myObjectOne = Car("2019","Black","Honda","1600cc","Yes")
myObjectOne.printDetails()
myObjectOne.updateSpeakers("No")
myObjectOne.updateColor("Metallic Black")
print("Data Updated")
myObjectOne.printDetails()


myObjectTwo = Car("2018","Blue","Audi","3200cc","Yes")
myObjectTwo.printDetails()
myObjectTwo.updateSpeakers("No")
myObjectTwo.updateColor("Red")
print("Data Updated")
myObjectTwo.printDetails()


myObjectThree = Car("2017","Grey","Toyota","1800cc","Yes")
myObjectThree.printDetails()
myObjectThree.updateSpeakers("No")
myObjectThree.updateColor("White")
print("Data Updated")
myObjectThree.printDetails()


myObjectFour = Car("2016","White","Mazda","900cc","No")
myObjectFour.printDetails()
myObjectFour.updateSpeakers("Yes")
myObjectFour.updateColor("Brown")
print("Data Updated")
myObjectFour.printDetails()


myObjectFive = Car("2015","Brown","Civic","1700cc","Yes")
myObjectFive.printDetails()
myObjectFive.updateSpeakers("No")
myObjectFive.updateColor("White")
print("Data Updated")
myObjectFive.printDetails()
