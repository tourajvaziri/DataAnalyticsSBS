# Create different variables that hold different types: int, float, str, bool and datetime

# The using the variables perform different operations.

# 1. int: i.e. add, multiplication. More info: https://www.w3schools.com/python/python_operators.asp


# 2. float: i.e. division, finding the floor (3.3 -> 3). More info: https://www.w3schools.com/python/python_operators.asp


# 3. str: i.e. replace ('samir' -> 'sameer'), characters count ('hello' -> 5), to lowercase ('BMW' -> 'bmw'). more info: https://www.w3schools.com/python/python_strings.asp


# 4. bool: i.e. compare two variables (a == b -> True). More info: https://www.w3schools.com/python/python_booleans.asp


# 5. datetime: create a datetime representation of your date of birth.  (Note: For working with datetime you first to need import it), More info: https://www.w3schools.com/python/python_datetime.asp
integer_var_1 = 10
>>> integer_var_2 = 5
>>> addition_result = integer_var_1 + integer_var_2
>>> multiplication_result = integer_var_1 * integer_var_2
>>> print(f"Integer Addition: {addition_result}")
Integer Addition: 15
>>> print(f"Integer Multiplication: {multiplication_result}")

Integer Multiplication: 50
>>> 


>>> float_var_1 = 7.5
>>> float_var_2 = 2.5
>>> division_result = float_var_1 / float_var_2
>>> floor_result = float_var_1 // float_var_2
>>> print(f"\nFloat Division: {division_result}")

Float Division: 3.0
>>> print(f"Float Floor: {floor_result}")
Float Floor: 3.0
>>> 




>>> string_var = "eyram"
>>> replace_result = string_var.replace("eyram", "sameer")
>>> character_count = len("hello")
>>> lowercase_result = "BMW".lower()
>>> print(f"\nString Replace: {replace_result}")

String Replace: sameer
>>> print(f"Character Count: {character_count}")
Character Count: 5
>>> print(f"To Lowercase: {lowercase_result}")
To Lowercase: bmw
>>> 



>>> bool_var_1 = True
>>> bool_var_2 = False
>>> comparison_result = bool_var_1 == bool_var_2
>>> print(f"\nBoolean Comparison: {comparison_result}")

Boolean Comparison: False
>>> 




>>> dob = datetime(2000, 1, 1)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    dob = datetime(2000, 1, 1)
NameError: name 'datetime' is not defined
>>> dob = datetime(2000, 1, 1)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    dob = datetime(2000, 1, 1)
NameError: name 'datetime' is not defined
>>> print(f"\nDate of Birth (datetime): {dob}")
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print(f"\nDate of Birth (datetime): {dob}")
NameError: name 'dob' is not defined
>>> 
