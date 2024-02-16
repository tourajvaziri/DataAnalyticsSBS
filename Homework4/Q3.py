# Create a variable of type Dictionary that holds information about vegetable names and their prices:
# 'Zucchini' -> $1.0   'Pepper' -> $1.2    'Onion' -> $1.4    'Carrot' -> $1.1
In [1]: vgDic = {"Zucchini":1.0, "Pepper":1.2, "Onion":1.4, "Carrot":1.1}

# Then using the Dictionary, 

# 1. print out the price for Onion
In [2]: print(vgDic['Onion'])
1.4

# 2. Update the price for Carrot to $1.15
In [3]: vgDic['Carrot'] = 1.15

# 3. Remove Pepper 
In [4]: del vgDic['Pepper']

# 4. Check if Zucchini exists, and if yes increase it's price by 10%
In [5]: if 'Zucchini' in vgDic:
   ...:         vgDic['Zucchini'] *= 1.1
