# Create two variables of type datetime with values of your choice for year, month, day etc. Then ouput the difference in years between the two variables.
# i.e.   2018,02,01  &  2016,01,03   ->  2         (2018-2016)
from datetime import datetime

# Create two datetime variables with values of your choice
date1 = datetime(2018, 2, 1)
date2 = datetime(2016, 1, 3)

# Calculate the difference in years
difference_in_years = (date1 - date2).days // 365

# Output the result
print("The difference in years is:", difference_in_years)
