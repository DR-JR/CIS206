# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 16:36:28 2026

@author: indig
"""
from employee import Employee


emp1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
emp2 = Employee("Mark Jones", 39119, "IT", "Programmer")
emp3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

for emp in [emp1, emp2, emp3]:
    print(emp)
    print()