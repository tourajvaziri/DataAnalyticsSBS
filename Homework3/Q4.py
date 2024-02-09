# Write code to output the count of emails by source (Yahoo or Gmail) and overall count (combined).
# Example data: ‘sameer@yahoo.com, SUE@GMAIL.com, eyram@gmail.com, Andrea@Yahoo.com,.....’
# Output: ‘Yahoo Emails: 2, Gmail Emails: 2, Total Emails: 4’

In [17]: emails = 'sameer@yahoo.com, SUE@GMAIL.com, eyram@gmail.com, Andrea@Yahoo.com'

In [18]: yahoo_count = 0

In [19]: google_count = 0

In [20]: for email in emails.split(','):
    ...:     if '@yahoo.com' in email.lower():
    ...:         yahoo_count +=1
    ...:     elif "gmail" in email.lower():
    ...:         google_count += 1
    ...:

In [21]: total_count = yahoo_count + google_count

In [22]: yahoo_count
Out[22]: 2

In [23]: google_count
Out[23]: 2

In [24]: total_count
Out[24]: 4
