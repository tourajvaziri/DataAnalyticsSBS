# Create a variable of type list that contains these four vegetable names: Zuchhini, Tomato, Pepper, Onion
In [6]: vegetables = ["Zucchini", "Tomato", "Pepper", "Onion"]

# Then using the list variable perform the following,

# 1. Print all the vegetable names contain in it
In [7]: print(vegetables)
['Zucchini', 'Tomato', 'Pepper', 'Onion']

# 2. Add a new vegetable (Potato) to the end of the list
In [8]: vegetables.append("Potato")

# 3. Access the element 'Pepper'
In [9]: print(vegetables[2])
Pepper

# 4. Remove the element 'Zucchini'
In [10]: vegetables.remove("Zucchini")

# 5. Update the element 'Onion' to 'Yellow Onion'
In [11]: vegetables[3] = "Yellow Onion"

# 6. Print out the number of vegetables in the list (i.e size of the list)
In [12]: print(len(vegetables))
4

# 7. Sort the vegetables alphabitically
In [13]: vegetables.sort()
