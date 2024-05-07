#!/usr/bin/env python3
class Dog: 
    def __init__(self, color, breed):
        self.color = color
        self.breed = breed

    def get_color(self):
        return self.color
    
    def get_breed(self):
        return self.breed

if __name__ == "__main__": 
    dog_breed = input("Enter the breed of the dog: ")
    dog_color = input("Enter the color of the dog: ")
    dog = Dog(dog_color, dog_breed)
    print(dog.get_color())
    print(dog.get_breed())
