# Write code to output the count of emails by source (Yahoo or Gmail) and overall count (combined).
# Example data: ‘sameer@yahoo.com, SUE@GMAIL.com, eyram@gmail.com, Andrea@Yahoo.com,.....’
# Output: ‘Yahoo Emails: 2, Gmail Emails: 2, Total Emails: 4’
>>> emailsData = 'sameer@yahoo.com,sue@GMAIL.com,Andrea@gmail.com,Eyram@Yahoo.com'
>>> emailsData = emailsData.lower()
>>> emailsData.count('gmail')
2
>>> emailsData.count('yahoo')
2
>>> print("Number of gmail accounts is 2, Number of yahoo accounts is 2 and total number of emails being4")
Number of gmail accounts is 2, Number of yahoo accounts is 2 and total number of emails being4
>>> 
