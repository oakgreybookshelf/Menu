#Brittny and Elsie

import menuitem
import menu

def main():
    mymenu = menu.Menu()
    
    menu1 = menuitem.MenuItem("hamburger", 450, 10)
    menu2 = menuitem.MenuItem("hot dog", 300, 9)
    menu3 = menuitem.MenuItem("soda", 300, 5)
    
    mymenu.additem(menu1)
    mymenu.additem(menu2)
    mymenu.additem(menu3)
    
    mymenu.print_menu()
    
    
    total = mymenu.calorie_total()
    print()
    print("The total calories is", total)
    

    
    
main()