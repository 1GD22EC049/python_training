class creation
class city:
    def addCityDetails(self,name,country):
        self.name = name
        self.country = country
    def printCityDetails(self):
        print("City Name:" + self.name)
        print("Country:" + self.country)
#object creation
delhi = city()
# calling the method
delhi.addCityDetails("delhi","India") 
delhi.printCityDetails()

mumbai = city()
# calling the method
mumbai.addCityDetails("mumbai","India") 
mumbai.printCityDetails()
from abc import ABC,abstractmethod
class Person():
    cityName = "india"
    def printName(self,name):
        print(name)
class Thanu(Person):
    def printDetails(self):
        print("some message")
obj = Thanu()
obj.cityName = "london"
obj.printName("thanu")                
  