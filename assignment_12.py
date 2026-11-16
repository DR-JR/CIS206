# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 16:38:59 2026

@author: indig
"""

class Patient:
    
    def __init__(self, first_name="", middle_name="", last_name="", address="", city="", state="", zipcode="", phone="", em_contact_name="", em_contact_phone=""):
        
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.phone = phone
        self.em_contact_name = em_contact_name
        self.em_contact_phone = em_contact_phone
        
    def set_first_name(self, first_name):
        self.first_name = first_name
    def set_middle_name(self, middle_name):
        self.middle_name = middle_name
    def set_last_name(self, last_name):
        self.last_name = last_name
    def set_address(self, address):
        self.address = address
    def set_city(self, city):
        self.city = city
    def set_state(self, state):
        self.state = state
    def set_zipcode(self, zipcode):
        self.zipcode = zipcode
    def set_phone(self, phone):
        self.phone = phone
    def set_em_contact_name(self, em_contact_name):
        self.em_contact_name = em_contact_name
    def set_em_contact_phone(self, em_contact_phone):
        self.em_contact_phone = em_contact_phone
    
    def get_first_name(self):
        return self.first_name
    def get_middle_name(self):
        return self.middle_name
    def get_last_name(self):
        return self.last_name
    def get_address(self):
        return self.address
    def get_city(self):
        return self.city
    def get_state(self):
        return self.state
    def get_zipcode(self):
        return self.zipcode
    def get_phone(self):
        return self.phone
    def get_em_contact_name(self):
        return self.em_contact_name
    def get_em_contact_phone(self):
        return self.em_contact_phone
    
    def __str__(self):
        return (f"First Name: {self.first_name}\n"
                f"Middle Name: {self.middle_name}\n"
                f"Last Name: {self.last_name}\n"
                f"Address: {self.address}\n"
                f"City: {self.city}\n"
                f"State: {self.state}\n"
                f"Zipcode: {self.zipcode}\n"
                f"Phone: {self.phone}\n"
                f"Emergency Contact: {self.em_contact_name}\n"
                f"Emergency Contact Phone: {self.em_contact_phone}")

class Procedure:
    
    def __init__(self, proc_name = "", proc_date = "", practitioner = "", charges = ""):
        
        self.proc_name = proc_name
        self.proc_date = proc_date
        self.practitioner = practitioner
        self.charges = charges
    
    def set_proc_name(self, proc_name):
        self.proc_name = proc_name
    def set_proc_date(self, proc_date):
        self.proc_date = proc_date
    def set_practitioner(self, practitioner):
        self.practitioner = practitioner
    def set_charges(self, charges):
        self.charges = charges
    
    def get_proc_name(self):
        return self.proc_name
    def get_proc_date(self):
        return self.proc_date
    def get_practitioner(self):
        return self.practitioner
    def get_charges(self):
        return self.charges
    
    def __str__(self):
        return (f"Procedure Name: {self.proc_name}\n"
                f"Procedure Date: {self.proc_date}\n"
                f"Practitioner: {self.practitioner}\n"
                f"Total Charges: {self.charges}")
    
proc_1 = Procedure("Physical Exam", "11/15/2026", "Dr. Irvine", "$250.00")
proc_2 = Procedure("X-ray", "11/15/2026", "Dr. Jamison", "$500.00")
proc_3 = Procedure("Blood test", "11/15/2026", "Dr. Smith", "$200.00")

for proc in [proc_1, proc_2, proc_3]:
    print(proc)
    print()