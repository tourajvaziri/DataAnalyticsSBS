# Write code to print all the lines in the file carData.csv. (Check current directory for the file) 
# Note: Call file.close() after your code to properly close the resource

In [11]: file = open("carData.csv")

In [12]: for line in file:
    ...:     print(line)
    ...:
carmodel,price,year
fiat,$14000,2017
BMW,$20000,2020
fiat,$17000,2019
bmw,$19000,2018
BMW,$25000,2021
fiat,$10000,2010
Toyota,$22000,2006

In [13]: file.close()
