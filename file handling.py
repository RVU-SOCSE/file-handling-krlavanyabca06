Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import pandas as pd
>>>  df = pd.read_csv('C:/Users/RVUW291/Desktop/5prog_1experience.csv')
...  
SyntaxError: unexpected indent
>>> df = pd.read_csv('C:/Users/RVUW291/Desktop/5prog_1experience.csv')
>>> # 1. Display the content of the file
>>> print("Full Data:")
Full Data:
>>> print(df)
   YearsExperience
0              1.1
1              1.3
2              1.5
3              2.0
4              2.2
5              2.9
6              3.0
7              3.2
8              3.2
>>> # 2. Find total number of rows and columns
>>> rows, columns = df.shape
>>> print("\nNumber of rows:", rows)

Number of rows: 9
>>> print("Number of columns:", columns)
Number of columns: 1
>>> # 3. Calculate the length of the dataframe (number of rows)
>>> print("\nLength of dataframe:", len(df))

Length of dataframe: 9
>>> # 4. Display the first 2 rows only
>>> print("\nFirst 2 rows:")

First 2 rows:
>>> print(df.head(2))
   YearsExperience
0              1.1
1              1.3
