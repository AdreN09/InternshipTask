# Aggregate data
*by Adrian Krawczyk*
***

## Table of Contents
- [General Info](#general_info)
- [Technologies Used](#tec)
- [Results](#results)
- [Executing Info](#exeInfo)
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

- Default agregating of two csv files

After starting the program and typing the command: `join file_path file_path column_name` ,we get data frame from both files.

In my case: `join C:\InternshipTask\Pokemon1.csv C:\InternshipTask\Pokemon2.csv Name`

![Data frame from both files](/Images/join.png)

After executing the program, we can also check the generated data in `dataFrame.csv`.

![Data frame from both files in csv](/Images/csv4.png)

- Agregating of two csv files with join type

  - Join type: inner
  
  After starting the program and typing the command: `join file_path file_path column_name inner` ,we get data frame with inner join type from both files.
  
  In my case: `join C:\InternshipTask\Products.csv C:\InternshipTask\Customers.csv Product_ID inner`
  
  ![Data frame with inner join type](/Images/inner.png)
  
  - Join type: left
  
  After starting the program and typing the command: `join file_path file_path column_name left` ,we get data frame with left join type from both files.
  
  In my case: `join C:\InternshipTask\Products.csv C:\InternshipTask\Customers.csv Product_ID left`
  
  ![Data frame with left join type](/Images/left.png)
  
  - Join type: right
  
  After starting the program and typing the command: `join file_path file_path column_name right` ,we get data frame with right join type from both files.
  
  In my case: `join C:\InternshipTask\Products.csv C:\InternshipTask\Customers.csv Product_ID right`
  
  ![Data frame with right join type](/Images/right.png)
## <a name="exeInfo" /> Executing Information
The program script is in the file: `InternshipTask.py`

To test the operation of the program, sample data was added in csv files:
- four argumets: `Pokemon1.csv`, `Pokemon2.csv`
- five argumets (with join type): `Customers.csv`, `Products.csv`

To run the application properly, Python packages (pandas) have to be installed on your PC.

The optional saving of the data frame is included in the file: `dataFrame.csv`

The other information about the file in the repository:
- /Images - images used in the README.md file are stored
## <a name="data" /> Data
### Archive
The archive with the data about Pokemons used in this project can be reached by [the following link](https://gist.github.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6).

In order to test the operation of the program, this database has been divided into two smaller files.
