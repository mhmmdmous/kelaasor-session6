from math import gcd

class Fraction:
    def __init__(self, numerator = 0, denominator = 1):
        if denominator == 0:  
            raise ValueError("Denominator cannot be zero.")        
        self.__numerator = numerator
        self.__denominator = denominator

    def __str__(self):
       return f"{self.__numerator}/{self.__denominator}"
    
    def __simplify(self):
        bmm = gcd(self.__numerator, self.__denominator)
        self.__numerator = int(self.__numerator / bmm)
        self.__denominator = int(self.__denominator / bmm)
        if self.__denominator < 0:
            self.__numerator *= -1
            self.__denominator *= -1
    
    def set_value(self, numerator, denominator, *args, **kwargs):
        if denominator == 0:  
            raise ValueError("Denominator cannot be zero.")        
        if isinstance(numerator, int):
            self.__numerator = numerator
        elif isinstance(numerator, float):
            self.__numerator = self.float_to_fraction(numerator)[0]
            self.__denominator = self.float_to_fraction(numerator)[1]*self.__denominator
        if isinstance(denominator, int):
            self.__denominator = denominator
        elif isinstance(denominator, float):
            self.__denominator = self.float_to_fraction(denominator)[0]
            self.__numerator = self.float_to_fraction(denominator)[1]*self.__numerator
    
    @staticmethod    
    def float_to_fraction(num):
        decimal_places = len(str(num).split(".")[1])
        denominator = 10 ** decimal_places  
        numerator = int(num * denominator)
        return [numerator, denominator]
    
    def __add__(self, other: 'Fraction'):
        return Fraction(
            self.__numerator * other.__denominator + self.__denominator * other.__numerator, 
            self.__denominator * other.__denominator
        )


frac3 = Fraction()
frac3.set_value(2.5, 3) 
frac2 = Fraction()
frac2.set_value(4, 3)

print(frac3)  
result = frac3 + frac2
print(result) 
