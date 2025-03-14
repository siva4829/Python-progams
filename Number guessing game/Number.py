import random as rd
import time

def randomNumbergenerator():
    while True:
        try:
            f=1
            x = eval(input("Enter one number: "))
            time.sleep(f)
            hell = "0123456789"
            t = rd.choice(hell)
            time.sleep(f)
            print("the system chosen number is",t)
            
            if x == int(t):
                time.sleep(3)
                print("Congrats! You're a winner!")
            else:
                time.sleep(f)
                print("Best of luck for next time!")
            time.sleep(f)

            v = input("Do you want to try again? (yes/no): ")
            if v == "yes":
                time.sleep(f)
                continue
            elif v == "no":
                time.sleep(f)
                print("Thanks for playing!")
                break
            else:
                time.sleep(f)
                print("Please enter 'yes' or 'no' in lowercase.")
        
        except ValueError:
            print("Please enter a valid number.")

randomNumbergenerator()
