class Discount:
    def __init__(self, value):
        self.value = value          
    
    def __call__(self, price):
        if isinstance(self.value, int):
            return (price - self.value) 
        elif isinstance(self.value, str):
            new_value = int(self.value.replace("%", ""))
            return price - (price* new_value / 100)
    
d1 = Discount(20) # fixed -20 dollar discount 
print(d1(100)) # prints 80
print(d1(200)) # prints 180

d2 = Discount("20%") # 20 percent discount
print(d2(100)) # prints 80
print(d2(200)) # prints 160