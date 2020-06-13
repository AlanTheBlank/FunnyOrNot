import os

funny = False
# Holy sh*t are you actually gonna run this?
choice = input("WARNING: This program will scan your files in the current working directory and delete anything not funny.  Type 'Yes' to continue")
if('yes' in choice):
    for x in os.listdir("."):
        if(not os.path.isdir(x)):
            if(not funny):
                f = open(x)
                print("bruh " + x + " isn't funny")
                f.close()
                os.remove(x)
            else:
                print("Bruh " + x + "is actually kinda funny")