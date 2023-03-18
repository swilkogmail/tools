#!/usr/bin/python3
my_emails={}

my_emails['steve'] = 's@gmail.com'
my_emails['barry'] = 'b@gmail.com'
my_emails['dave'] = 'd@gmail.com'
my_emails['nick'] = 'n@gmail.com'

print(my_emails)

del my_emails['nick']
my_emails['dalton'] = 'd@gmail.com'

print(my_emails)

# return list of keys
print(list(my_emails.keys()))
# return list of values
print(list(my_emails.values()))
# return list of tuples called
pairs = list(my_emails.items())
print(pairs) # returns a list of tuples
