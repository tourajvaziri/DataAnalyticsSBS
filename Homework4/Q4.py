# Give the variable emails containing a list of 24 yahoo and 33 gmail email addresses:
emails = ['user3@yahoo.com', 'user25@gmail.com', 'user18@yahoo.com', 'user9@yahoo.com', 'user4@yahoo.com', 'user27@gmail.com', 'user5@gmail.com', 'user12@gmail.com', 'user5@yahoo.com', 'user11@gmail.com', 'user20@gmail.com', 'user1@yahoo.com', 'user31@gmail.com', 'user16@gmail.com', 'user22@yahoo.com', 'user6@yahoo.com', 'user6@gmail.com', 'user8@yahoo.com', 'user20@yahoo.com', 'user32@gmail.com', 'user30@gmail.com', 'user13@gmail.com', 'user4@gmail.com', 'user13@yahoo.com', 'user19@gmail.com', 'user7@gmail.com', 'user29@gmail.com', 'user23@gmail.com', 'user8@gmail.com', 'user1@gmail.com', 'user12@yahoo.com', 'user14@gmail.com', 'user14@yahoo.com', 'user15@yahoo.com', 'user15@gmail.com', 'user24@gmail.com', 'user9@gmail.com', 'user17@yahoo.com', 'user2@gmail.com', 'user21@yahoo.com', 'user3@gmail.com', 'user11@yahoo.com', 'user7@yahoo.com', 'user18@gmail.com', 'user22@gmail.com', 'user16@yahoo.com', 'user10@gmail.com', 'user26@gmail.com', 'user17@gmail.com', 'user28@gmail.com', 'user24@yahoo.com', 'user33@gmail.com', 'user10@yahoo.com', 'user19@yahoo.com', 'user2@yahoo.com', 'user21@gmail.com', 'user23@yahoo.com']

# You task is to create a variable of type Dictionary that stores the type of email and total count as key value pairs:
# i.e   yahoo -> 24     gmail -> 33

# Hint:
# Start by defining a variable of type Dictionary that has two keys: 'yahoo' and 'gmail' and both values set to 0 initially.
# Then loop through the emails list: for each email address check if it is 'yahoo' or 'gmail':
#   If 'yahoo', update the 'yahoo' key in the dictionary, set the value:  current value + 1.
#   If 'gmail', update the 'gmail' key in the dictionary, set the value:  current value + 1.