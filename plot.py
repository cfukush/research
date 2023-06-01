import colorsys
from http.cookiejar import CookiePolicy
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


print("This program make graph.")
print("How to use this program (1 or 2)")
print("1. Open file   2. Enter data")
answer1 = input()

x=[]
y=[]

while not (answer1 == "1" or answer1 == "2"):
    print("Please enter 1 or 2")
    answer1 = input()
else:
    if (answer1 == "1"):
        print("Enter the file path and name")
        file_name = input()
        if ("xlsx" in file_name):    
            df = pd.read_excel(file_name)
            print(df)
            print("Name of the header you want on the x-axis.")
            headerx = input()
            print("Name of the header you want on the y-axis")
            headery = input()
            x = df[headerx]
            y = df[headery]
            df.plot(kind='scatter', x=headerx, y=headery)
        elif ("csv" in file_name):
            df = pd.read_csv(file_name)
            print(df)
            print("Name of the header you want on the x-axis.")
            headerx = input()
            print("Name of the header you want on the y-axis")
            headery = input()
            x = df[headerx]
            y = df[headery]
            df.plot(kind='scatter', x=headerx, y=headery)
        else:
            df = pd.read_table(file_name, sep=' ')
            print(df)
            print("Name of the header you want on the x-axis.")
            headerx = input()
            print("Name of the header you want on the y-axis")
            headery = input()
            x = df[headerx]
            y = df[headery]
            print(x)
            print(y)
            df.plot(kind='scatter', x=headerx, y=headery)
    elif (answer1 == "2"):
        try:
            for i in range(10000):
                print("Enter x[",i+1,"] value.")
                x.append(float(input()))
                print("Enter y[",i+1,"] value")
                y.append(float(input()))
        except KeyboardInterrupt:
            print("end")
        plt.scatter(x,y)

plt.grid()  
plt.pause(0.1)


#Set axis-label
print("Do you want to see axis-label? (yes/no)")
answer3 = input()

while not (answer3 == "yes" or answer3 == "no"):
    print("\aPlease enter yes or no")
    answer3 = input()
else:
    if (answer3 == "yes"):
        print("x-label")
        namex = input()
        plt.xlabel(namex)
        print("y-label")
        namey = input()
        plt.ylabel(namey)
    elif (answer3 == "no"):
        pass

plt.pause(0.1)


#Save graph
print("Do you want to save graph? (yes/no)")
answer4 = input()

while not (answer4 == "yes" or answer4 == "no"):
    print("Do you want to save graph? (yes/no)")
    answer4 = input()
else:
    if (answer4 == "yes"):
        print("Enter a file name with .png:")
        save_file = input()
        plt.savefig(save_file,)
    elif (answer4 == "no"):
        pass

plt.show()

