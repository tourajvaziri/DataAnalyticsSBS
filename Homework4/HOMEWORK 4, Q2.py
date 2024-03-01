Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Create a list of vegetable names

vegetable_list = ["Zucchini", "Tomato", "Pepper", "Onion"]

# 1. Print all the vegetable names in the list

print("Vegetable names in the list:", vegetable_list)
Vegetable names in the list: ['Zucchini', 'Tomato', 'Pepper', 'Onion']

# 2. Add a new vegetable (Potato) to the end of the list
vegetable_list.append("Potato")

print("List after adding Potato:", vegetable_list)
List after adding Potato: ['Zucchini', 'Tomato', 'Pepper', 'Onion', 'Potato']

# 3. Access the element 'Pepper'

print("Element at index 2 (Pepper):", vegetable_list[2])
Element at index 2 (Pepper): Pepper

# 4. Remove the element 'Zucchini'

vegetable_list.remove("Zucchini")

print("List after removing Zucchini:", vegetable_list)
List after removing Zucchini: ['Tomato', 'Pepper', 'Onion', 'Potato']

# 5. Update the element 'Onion' to 'Yellow Onion'

index_onion = vegetable_list.index("Onion")
vegetable_list[index_onion] = "Yellow Onion"

print("List after updating Onion to Yellow Onion:", vegetable_list)
List after updating Onion to Yellow Onion: ['Tomato', 'Pepper', 'Yellow Onion', 'Potato']

# 6. Print out the number of vegetables in the list (i.e. size of the list)
print("Number of vegetables in the list:", len(vegetable_list))
Number of vegetables in the list: 4

# 7. Sort the vegetables alphabetically
vegetable_list.sort()
print("List after sorting alphabetically:", vegetable_list)
List after sorting alphabetically: ['Pepper', 'Potato', 'Tomato', 'Yellow Onion']
>>> 