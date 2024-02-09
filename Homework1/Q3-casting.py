# Cast between different types. More info: https://www.w3schools.com/python/python_casting.asp

# 1. Cast a string representation of int to int. i.e.  '35' -> 35


# 2. Cast a string representation of float to float. i.e. '23.3' -> 23.3


# 3. Cast int to string: i.e 45 -> '45'


# 4. Cast a string representation of datetime to datetime. i.e. '2018-02-07' -> equivalent datetime type. More info: https://www.programiz.com/python-programming/datetime/strptimestring_int = '35'
>>> integer_value = int(string_int)
>>> print(integer_value)
35
>>> 
>>> string_float = '23.3'
>>> float_value = float(string_float)
>>> print(float_value)
23.3
>>> 
>>> integer_number = 45
>>> string_number = str(integer_number)
>>> print(string_number)
45
>>> 
>>> string_datetime = '2018-02-07'
>>> from datetime import datetime
>>> date_string = "2018-02-07"
>>> print("date_string =", date_string)
date_string = 2018-02-07
>>> print("type of date_string =", type(date_string))
type of date_string = <class 'str'>
>>> date_object = datetime.strptime(date_string, "%d %m, %Y")
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    date_object = datetime.strptime(date_string, "%d %m, %Y")
  File "C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python39_64\lib\_strptime.py", line 568, in _strptime_datetime
    tt, fraction, gmtoff_fraction = _strptime(data_string, format)
  File "C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python39_64\lib\_strptime.py", line 349, in _strptime
    raise ValueError("time data %r does not match format %r" %
ValueError: time data '2018-02-07' does not match format '%d %m, %Y'
>>> datetime.strptime('2018-02-07', "%Y-%m-%d")
datetime.datetime(2018, 2, 7, 0, 0)
