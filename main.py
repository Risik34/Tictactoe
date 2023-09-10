import game
import time
import os


if __name__=="__main__":
   print("\n\t\tWELCOME TO ..."+"TIC_TAC_TOE")
  
   time.sleep(1)
   
   

   while True:
     game.printer()
     game.addx(input("\nEnter row for X: "), input ("Enter column for X: "))
     os.system("clear")
     game.printer()
     game.addo(input("\nEnter row for O: "), input ("Enter column for O: "))
     os.system("clear")



     
