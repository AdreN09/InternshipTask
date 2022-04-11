# Intership Task
# Autor: Adrian Krawczyk

import pandas as pd

# file_path = 'D:\Python\Data\pokemon.csv'

print("Internship Task")
print("To execute the program, execute the command: join file_path file_path column_name join_type")
command = input("Your command: ")
if "join" in command:
    command_sp = command.split(" ")
    file_path1 = pd.read_csv(command_sp[1])
    print(file_path1)

else:
    print("You can't use this command :/")


