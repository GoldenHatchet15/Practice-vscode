import random

#print("Loaded random_number module")

class RandomNumber:
    @staticmethod
    def random_number():
        return random.randint(1, 5)

    @staticmethod
    def two_digit_number():
        num = random.randint(0,99)
        if num < 10 and num > 0:
            return 
            

    @staticmethod
    def three_digit_number():
        return random.randint(000, 999)

#print("RandomNumber class defined with methods:", dir(RandomNumber))

