from  ex1 import Greeting
from ex2 import rectangle
from ex3 import Equation_Calulator
from ex4 import HundreadCounter
from ex5 import LucktNuymberGame

print(" ======= Tp2 Python OOP=======")
print(" Menu ")
print("1. Greeting")
print("2. Rectangle")
print("3. Equation Calculator")
print("4. Hundred Counter")
print("5. Lucky Number Game")
print(" 0 . Exit")
print(" ========================")

    
choice = int(input(" Enter your choice :"))
if choice == 1:
            Greeting()
            
elif choice == 2:
            rectangle()
            
elif choice == 3:
            Equation_Calulator()
            
elif choice == 4:
            HundreadCounter()
            
elif choice == 5:
            LucktNuymberGame()
            
elif choice == 0:
            print(" Exit")
            
else:
            print(" Invalid choice. Please try again.")
