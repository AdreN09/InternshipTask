# Internship Task
# Author: Adrian Krawczyk

import pandas as pd

# testing data for 4 arguments
# Pokemon1.csv
# Pokemon2.csv
# examples for using:
# join C:\InternshipTask\Pokemon1.csv C:\InternshipTask\Pokemon2.csv Name

# testing data for 5 arguments
# Customers.csv
# Products.csv
# examples for using:
# join C:\InternshipTask\Products.csv C:\InternshipTask\Customers.csv Product_ID
# join C:\InternshipTask\Products.csv C:\InternshipTask\Customers.csv Product_ID inner
# join C:\InternshipTask\Products.csv C:\InternshipTask\Customers.csv Product_ID left
# join C:\InternshipTask\Products.csv C:\InternshipTask\Customers.csv Product_ID right


print("Internship Task")
print("To execute the program, execute the command: join file_path file_path column_name join_type")
command = input("Your command: ")
command_sp = command.split(" ")

def read():
    if ".csv" in command_sp[1]:
        file_path1 = pd.read_csv(command_sp[1])
        if ".csv" in command_sp[2]:
            file_path2 = pd.read_csv(command_sp[2])
            if (command_sp[3] in file_path1) & (command_sp[3] in file_path2):
                df = pd.concat([file_path1, file_path2])
                df.to_csv("C:\InternshipTask\dataFrame.csv")
                print(df)
            else:
                print("Name of column: '" + command_sp[3] + "' doesn't exist in both csv's files! Try again.")
        else:
            print("Argument '" + command_sp[2] + "' is wrong! Try again.")
    else:
        print("Argument '" + command_sp[1] + "' is wrong! Try again.")

def join_type():
    if ".csv" in command_sp[1]:
        file_path1 = pd.read_csv(command_sp[1])
        if ".csv" in command_sp[2]:
            file_path2 = pd.read_csv(command_sp[2])
            if (command_sp[3] in file_path1) & (command_sp[3] in file_path2):
                if "inner" in command_sp[4]:
                    df_inner = pd.merge(file_path1, file_path2, on=command_sp[3])
                    df_inner.to_csv("C:\InternshipTask\dataFrame.csv")
                    print(df_inner)
                elif "left" in command_sp[4]:
                    df_left = pd.merge(file_path1, file_path2, on=command_sp[3], how='left')
                    df_left.to_csv("C:\InternshipTask\dataFrame.csv")
                    print(df_left)
                elif "right" in command_sp[4]:
                    df_right = pd.merge(file_path1, file_path2, on=command_sp[3], how='right')
                    df_right.to_csv("C:\InternshipTask\dataFrame.csv")
                    print(df_right)
                else:
                    print("Argument '" + command_sp[4] + "' is wrong! Try again.")
            else:
                print("Name of column:  '" + command_sp[3] + "' doesn't exist in both csv files! Try again.")
        else:
            print("Argument '" + command_sp[2] + "' is wrong! Try again.")
    else:
        print("Argument '" + command_sp[1] + "' is wrong! Try again.")

def main():
    if "join" in command:
        if len(command_sp) == 4:
            read()
        elif len(command_sp) == 5:
            join_type()
        else:
            print("Wrong numbers of arguments! Try again.")
    else:
        print("You can't use this command :/")

main()
