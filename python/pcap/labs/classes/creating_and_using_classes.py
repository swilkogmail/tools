#!/usr/bin/python3
from employee import Employee
from manager import Manager

emp101 = Employee('Steve','Wilkins','Lead Data Guy')

print(emp101.email_signature())


man101 = Manager('Barry','Brain','Head Data Guy')

print(man101.run_next_meeting())