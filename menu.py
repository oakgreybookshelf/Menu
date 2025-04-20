#Brittny and Elsie

import menuitem

class Menu:
    def __init__(self):
        self.__menulist = []
        
    def additem(self, item):
       
        self.__menulist.append(item)
            
    
    def calorie_total(self):
        total = 0
        for item in self.__menulist:
            total = total + item.get_calories()
        return total
            
            
            
            
    def print_menu(self):
        for item in self.__menulist:
            print(item)
    