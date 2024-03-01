Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> vegetable_info = [
    ("Zucchini", "Croatia"),
    ("Tomato", "Zimbabwe"),
    ("Pepper", "India"),
    ("Onion", "Ghana")
    ]
>>> # Accessing the tuple for Tomato
>>> tomato_tuple = vegetable_info[1]
>>> # Printing the country of origin for Tomato
>>> print("The country of origin for Tomato is:", tomato_tuple[1])
The country of origin for Tomato is: Zimbabwe
>>> 