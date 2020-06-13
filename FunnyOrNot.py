import os
import sys

funny = False
# Holy sh*t are you actually gonna run this?
choice = input("WARNING: This program will scan your files in the current working directory and delete anything not funny.  Type 'Yes' to continue\n")
if('yes'.upper() in choice.upper()):
    for x in os.listdir("."):
        if(not os.path.isdir(x) and x != sys.argv[0]):
            if(not funny):
                f = open(x)
                print("bruh " + x + " isn't funny")
                f.close()
                os.remove(x)
            else:
                print("Bruh " + x + "is actually kinda funny")