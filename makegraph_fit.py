
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
            #sheet_name = input()
            #header = int(input())
            #col1 = int(input())
            #col2 = int(input())
            #df1 = pd.read_excel(file_name, sheet_name,usecols=[col1, col2], header=header)
            #print(df1)
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
        """    
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
        """
        plt.scatter(x,y)



#Fitting and make graph
a,b = np.polyfit(x,y,1)
line = np.poly1d(np.polyfit(x,y,1))(x)

print("Slope:",a, "Intercept",b)
plt.plot(x,line, color="r")
plt.pause(0.1)

#Graph option
print("Do you want to set log?")
print("1. Set logy and Set logx. \n 2. Set logy. \n 3. No.")
answer2 = (input())

while not (answer2 == "1" or "2" or "3"):
    print("\aPlease enter the 1, 2 or 3.")
    answer2 = int(input())
else:
    if (answer2 == "1"):
        plt.cla()
        plt.yscale('log')
        plt.xscale('log')
        logx = [np.log10(i) for i in x]
        logy = [np.log10(i) for i in y]
        axy, bxy = np.polyfit(logx, logy, 1)
        #linear = [pow(10,(pow(10,bxy) * pow(10, pow(xvalue, axy)))) for xvalue in x]
        linear = [pow(10,bxy)*pow(xvalue,axy) for xvalue in x]
        plt.scatter(x,y)
        plt.plot(x, linear, color='r')
        print("Slpope:", axy)
        print("Constant:", pow(10,bxy)) 
    elif (answer2 == "2"):
        npx = np.array(x)
        npy = np.array(y)
        plt.cla()    
        plt.yscale('log')
        logy = np.log10(npy)
        ay, by = np.polyfit(npx,logy,1)
        linear = [pow(10,by) * pow(10,(ay*xvalue)) for xvalue in x]
        print("Slope:", ay, "Intercept:", by)
        plt.scatter(npx,npy)
        plt.plot(npx, linear, color='r')
    elif (answer2 == "3"):
        pass

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
