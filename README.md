# InternshipTask - aggregate data
*by Adrian Krawczyk*
***
This project was made for the recruitment task.
## Table of Contents
- [General Info](#general_info)
- [Technologies Used](#tec)
- [Results](#results)
- [Executing info](#exeInfo)
- [Data](#data)
## <a name="general_info" /> General Information
The aim of the project was creating a program which would be able to aggregate data from two csv files. 
By adding an additional argument, it is possible to concatenate data using the join type (inner, left, right).
Additionally, it is possible to save the created data frame to a csv file.

The program is executed with the command: join file_path file_path column_name join_type
## <a name="tec" /> Technologies Used
- Python 3.9
- Python library - pandas 1.3.1
## <a name="results" /> Results
In this chapter, I would like to demonstrate a few screenshots of the program's execution.
## <a name="exeInfo" /> Executing info
The program script is in the file: `InternshipTask.py`

To test the operation of the program, sample data was added in csv files:
- four argumets: `Pokemon1.csv`, `Pokemon1.csv`
- five argumets (with join type): `Customers.csv`, `Products.csv`

To run the application properly, Python packages (pandas) have to be installed on your PC.

The optional saving of the data frame is included in the file: `dataFrame.csv`
## <a name="data" /> Data
### Archive
The archive with the data about Pokemons used in this project can be reached by [the following link](https://gist.github.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6).

In order to test the operation of the program, this database has been divided into two smaller files.
