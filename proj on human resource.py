import pandas as pd
import matplotlib.pyplot as plt
from tkinter import messagebox as msg

human=pd.read_csv("humantraf.csv",index_col=0)
while(True):
    print("\n\n\t\t\t---- Main Menu ----\n")
    print("1. Fetch data")
    print("2. Dataframe Statistics")
    print("3. Display Records")
    print("4. Working on Records")
    print("5. Search specific row/column")
    print("6. Data Visualization")
    print("7. save the changes done in csv file")
    print("8. Exit")
    ch=int(input("\nEnter your choice here = "))
    if ch==1:
        human=pd.read_csv("humantraf.csv",index_col=0)
        print("\ndata fetched successfully\n")
    elif ch==2:
        while (True):
            print("\n\n\t\t\t~~~~ Dataframe Statistics Menu ~~~~\n")
            print("1. Display the Transpose")
            print("2. Display all column names")
            print("3. Display the indexes")
            print("4. Display the shape")
            print("5. Display the dimension")
            print("6. Display the data types of all columns")
            print("7. Display the size")
            print("8. Exit")
            ch2=int(input("\nEnter your choice here = "))
            if ch2==1:
                print(human.T)
            elif ch2==2:
                print(human.columns)
            elif ch2==3:
                print(human.index)
            elif ch2==4:
                print(human.shape)
            elif ch2==5:
                print(human.ndim)
            elif ch2==6:
                print(human.dtypes)
            elif ch2==7:
                print(human.size)
            elif ch2==8:
                break
            else:
                msg.showerror("invalid choice","you have entered invalid choice")
    elif ch==3:
        while(True):
            print("\n\n\t\t\t~~~~ Display Records Menu ~~~~\n")
            print("1. Top 5 Records")
            print("2. Bottom 5 Records")
            print("3. Specific number of records from the top")
            print("4. Specific number of records from the bottom")
            print("5. Details of a specific State")
            print("6. Exit")
            ch3=int(input("\nEnter your choice here = "))
            if ch3==1:
                print(human.head())
            elif ch3==2:
                print(human.tail())
            elif ch3==3:
                n=int(input("\nEnter how many records you want to display from the top = "))
                print(human.head(n))
            elif ch3==4:
                n=int(input("\nEnter how many records you want to display from the bottom = "))
                print(human.tail(n))
            elif ch3==5:
                st=input("\nEnter the state name for which you want to see the details = ")
                A=st.upper()
                print(human.loc[A])
            elif ch3==6:
                break
            else:
                msg.showerror("invalid choice","you have entered invalid choice")
    elif ch==4:
        while(True):
            print("\n\n\t\t\t~~~~ Working on Records Menu ~~~~\n")
            print("1. Insert a specific state Record")
            print("2. Delete a specific state Record")
            print("3. Update a specific state Record")
            print("4. Exit")
            ch4=int(input("\nEnter your choice here = "))
            if ch4==1:
                a=input("\nEnter state name here = ").upper()
                b=int(input("Enter number of males below 18 yrs = "))
                c=int(input("Enter number of females below 18 yrs = "))
                d=int(input("Enter number of males above 18 yrs = "))
                e=int(input("Enter number of females above 18 yrs = "))
                human.loc[a]=[b,c,d,e]
                print("Data successfully inserted")
            elif ch4==2:
                a=input("Enter state name whose data needs to be deleted = ").upper()
                human.drop([a],inplace=True)
                print("Data successfully deleted")
            elif ch4==3:
                a=input("Enter state name whose data needs to be updated = ").upper()
                b=int(input("Enter new number of males below 18 yrs = "))
                c=int(input("Enter new number of females below 18 yrs = "))
                d=int(input("Enter new number of males above 18 yrs = "))
                e=int(input("Enter new number of females above 18 yrs = "))
                human.loc[a]=[b,c,d,e]
                print("Data successfully updated")
            elif ch4==4:
                break
            else:
                msg.showerror("invalid choice","you have entered invalid choice")
    
    elif ch==5:
        while(True):
            print("\n\n\t\t\t~~~~ Search Menu ~~~~\n")
            print("1. Search for the details of a specific state")
            print("2. Search details of a specific column")
            print("3. Exit")
            ch6=int(input("\nEnter your choice here = "))
            if ch6==1:
                st=input("\nEnter the name of the city whose details you want to see = ").upper()
                print(human.loc[st])
            elif ch6==2:
                col=input("\nEnter column name whose details you want to see = ")
                print(human[col])
            elif ch6==3:
                break
            else:
                msg.showerror("invalid choice","you have entered invalid choice")
    elif ch==6:
        while(True):
            print("\n\n\t\t\t~~~~ Data Visualization Menu ~~~~\n")
            print("1. Line Plot")
            print("2. Vertical Bar Plot")
            print("3. Horizontal Bar Plot")
            print("4. Histogram")
            print("5. Exit")
            ch7=int(input("\nEnter your choice here = "))
            if ch7==1:
                n=int(input("\nHow many states from the top you want to plot? = "))
                df=human.head(n)
                mb=df['MBelow18']
                fb=df['FBelow18']
                ma=df['MAbove18']
                fa=df['FAbove18']
                s=df.index
                plt.plot(s,mb,label="Males below 18")
                plt.plot(s,fb,label="Females below 18")
                plt.plot(s,ma,label="Males Above 18")
                plt.plot(s,fa,label="Females Above 18")
                plt.title("Line Graph representing statewise numbers")
                plt.xlabel("STATES")
                plt.ylabel("COUNT OF MALES & FEMALES")
                plt.xticks(rotation=30)
                plt.legend()
                plt.grid(True)
                plt.show()
            elif ch7==2:
                n=int(input("\nHow many states from the top you want to plot? = "))
                df=human.head(n)
                df.plot(kind="bar")
                plt.title("Bar Graph representing statewise numbers")
                plt.xlabel("STATES")
                plt.ylabel("COUNT OF MALES & FEMALES")
                plt.show()
            elif ch7==3:
                n=int(input("\nHow many states from the top you want to plot? = "))
                df=human.head(n)
                df.plot(kind="barh")
                plt.title("Horizontal Bar Graph representing statewise numbers")
                plt.xlabel("COUNT OF MALES & FEMALES")
                plt.ylabel("STATES")
                plt.show()
            elif ch7==4:
                n=int(input("\nHow many states from the top you want to plot? = "))
                df=human.head(n)
                df.plot(kind="hist")
                plt.title("Bar Graph representing statewise numbers")
                plt.xlabel("STATES")
                plt.ylabel("COUNT OF MALES & FEMALES")
                plt.show()
            elif ch7==5:
                break
            else:
                msg.showerror("invalid choice","you have entered invalid choice")
    elif ch==8:
        break
    elif ch == 7:
        human.to_csv("humantraf.csv")
        print("\nchanges successfully done in csv file\n")
        print(human)
    else:
        msg.showerror("invalid choice","you have entered invalid choice")
