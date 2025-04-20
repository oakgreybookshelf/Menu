#Brittny and Elsie

import menuitem
import menu

def main():
    mymenu = menu.Menu()

    # take input for food item 1

    menuFood = input("Enter a food to add to the menu: ")
    menuFoodCalories = int(input("Enter the food calorie count "))
    menuFoodPrice = int(input("Enter the food price: "))
    
    menu1 = menuitem.MenuItem(menuFood, menuFoodCalories, menuFoodPrice)

    # take input for food item 2

    menuFood = input("Enter a food to add to the menu: ")
    menuFoodCalories = int(input("Enter the food calorie count "))
    menuFoodPrice = int(input("Enter the food price: "))
    
    menu2 = menuitem.MenuItem(menuFood, menuFoodCalories, menuFoodPrice)

    # take input for food item 3
    
    menuFood = input("Enter a food to add to the menu: ")
    menuFoodCalories = int(input("Enter the food calorie count "))
    menuFoodPrice = int(input("Enter the food price: "))
    
    menu3 = menuitem.MenuItem(menuFood, menuFoodCalories, menuFoodPrice)
    
    mymenu.additem(menu1)
    mymenu.additem(menu2)
    mymenu.additem(menu3)
    
    mymenu.print_menu()
    
    
    total = mymenu.calorie_total()
    print()
    print("The total calories is", total)
    

    
main()
