Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Create a dictionary of vegetable names and their prices

vegetable_prices = {
    'Zucchini': 1.0,
    'Pepper': 1.2,
    'Onion': 1.4,
    'Carrot': 1.1}

# 1. Print out the price for Onion
print("Price for Onion:", vegetable_prices['Onion'])
Price for Onion: 1.4

# 2. Update the price for Carrot to $1.15
vegetable_prices['Carrot'] = 1.15
print("Updated price for Carrot:", vegetable_prices['Carrot'])
Updated price for Carrot: 1.15

# 3. Remove Pepper
del vegetable_prices['Pepper']
print("Dictionary after removing Pepper:", vegetable_prices)
Dictionary after removing Pepper: {'Zucchini': 1.0, 'Onion': 1.4, 'Carrot': 1.15}

# 4. Check if Zucchini exists, and if yes, increase its price by 10%
if 'Zucchini' in vegetable_prices:
    vegetable_prices['Zucchini'] *= 1.1
    print("Updated price for Zucchini:", vegetable_prices['Zucchini'])
else:
    print("Zucchini does not exist in the dictionary.")
    
Updated price for Zucchini: 1.1
>>> 