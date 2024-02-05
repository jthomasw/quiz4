from abc import ABC, abstractmethod

class Pet(ABC):
        @abstractmethod
        def petName(self):
                pass
        
        @abstractmethod
        def petAge(self):
                pass
        
class Dog(Pet):
        def __init__(self, name , age):
                self.name = name
                self.age = age

        def display_bio(self):
                print(f"Your dogs name is {self.name}, and they are... woah! they are {self.age} years old!!!")
                
class Cat(Pet):
        def __init__(self, name, age):
                self.name = name
                self.age = age

        def display_bio(self):
                print(f"Your cats name is {self.name}, and they are... woah! they are {self.age} years old!!!")
                
def main(): 
        dog = Dog("Sparky",5)
        cat = Cat("Mittens", 3)

        dog.display_bio()
        
        cat.display_bio()

        if __name__ == '__main__':
            main()