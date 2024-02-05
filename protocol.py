from typing import Protocol, Optional

class PetProtocol(Protocol):
    def petName(self) -> str:
        pass
    
    def petAge(self) -> int:
        pass

class Pet:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

class Dog(Pet, PetProtocol):
    def display_bio(self):
        print(f"Your dog's name is {self.name}, and they are... woah! they are {self.age} years old!!!")

class Cat(Pet, PetProtocol):
    def display_bio(self):
        print(f"Your cat's name is {self.name}, and they are... woah! they are {self.age} years old!!!")

def main():
    dog = Dog("Sparky", 5)
    cat = Cat("Mittens", 3)

    dog.display_bio()
    cat.display_bio()

if __name__ == '__main__':
    main()