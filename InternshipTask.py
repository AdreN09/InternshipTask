# Intership Task
# Autor: Adrian Krawczyk

import pandas as pd

# file_path = 'D:\Python\Data\pokemon.csv'
# join C:\InternshipTask\Pokemon1.csv
# join C:\InternshipTask\Pokemon1.csv C:\InternshipTask\Pokemon2.csv

print("Internship Task")


def start():
    print("To execute the program, execute the command: join file_path file_path column_name join_type")
    command = input("Your command: ")
    if "join" in command:
        command_sp = command.split(" ")
        if ".csv" in command_sp[1]:
            file_path1 = pd.read_csv(command_sp[1])
            if ".csv" in command_sp[2]:
                file_path2 = pd.read_csv(command_sp[2])
                if (command_sp[3] in file_path1) & (command_sp[3] in file_path2):
                    df = pd.concat([file_path1, file_path2])
                    print(df)
                    print(df.columns)
                else:
                    print("Name of column:  " + command_sp[3] + " doesn't exist in both csv's files!")
                    start()
            else:
                print("Argument " + command_sp[2] + " is wrong!")
                start()
        else:
            print("Argument " + command_sp[1] + " is wrong!")
            start()
    else:
        print("You can't use this command :/")


start()
