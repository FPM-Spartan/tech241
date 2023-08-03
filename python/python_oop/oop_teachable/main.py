import customer
import employee
import random


if random.randint(0,1) == 0:
    my_person = customer.Customer('Jyoti' 'Suresh', 'Mumbai')
else:
    my_person = employee.Employee('Peter', 'Forbes', 'Marketing')

my_person.print()