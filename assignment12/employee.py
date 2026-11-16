# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 01:00:37 2026

@author: indig
"""

class Employee:
    
    def __init__(self, name="", id_number=0, department="", position=""):

        self.name = name
        self.id_number = id_number
        self.department = department
        self.position = position
    
    def set_name(self, name):
        self.name = name
    def set_id_number(self, id_number):
        self.id_number = id_number
    def set_department(self, department):
        self.department = department
    def set_position(self, position):
        self.position = position
    
    def get_name(self):
        return self.name
    def get_id_number(self):
        return self.id_number
    def get_department(self):
        return self.department
    def get_position(self):
        return self.position
    
    def __str__(self):
        return (f"Name: {self.name}\n"
                f"ID Number: {self.id_number}\n"
                f"Department: {self.department}\n"
                f"Position: {self.position}")
        
