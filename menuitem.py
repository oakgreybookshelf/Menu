#Brittny and Elsie

class MenuItem:
    def __init__(self, name, calories, price):
        self.__name = name
        self.__calories = calories
        self.__price = price
        
    def get_name(self):
        return self.__name
    
    def get_calories(self):
        return self.__calories
    
    def get_price(self):
        return self.__price
    
    def __str__(self):
        return "The menu item is " + str(self.__name) + ", the calories is " + str(self.__calories) + ", and the price is $" + str(self.__price)
    
    
    