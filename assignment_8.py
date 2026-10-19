# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 15:25:18 2026

@author: indig
"""


def rows_search(rows, header, x):
    
    if x == '3':
        q = input("Please enter any part of a company name to perform a search: ").lower()
        for n in rows:
            if q in rows[n]:
                return rows[n]
        
    elif x == '4':
        pass
        
    else:
        print("Unknown error. WEIRD :O")
        return
    
def rows_sorting(rows, header, x):
    
    if x == '1':
        cat = [1, 2, 9]
    
    elif x == '2':
        cat = [2, 1, 9]
    
    else:
        print("Unknown option. WEIRD! 8{D")
        return
    
    result = []
    for r in rows:
        row = []
        for c in cat:
            row.append(r[c])
        result.append(row)
        
    result.sort()
    
    header_result = []
    for c in cat:
        header_result.append(header[c])
        
    result.insert(0, header_result)
    for r in result:
        for v in r:
            print("|", f"{v:<40}", end=" ")
        print("|")

    
def customer_info_clean():
    with open("Northwind_Customers.txt", "r") as customers_txt:
        customers = customers_txt.readlines()
    
    header = []
    rows = []
    
    titles = customers[0].strip()[1:-1].split('","')
    for t in titles:
        header.append(t.strip())
        
    for c in customers[1:]:
        if c.strip() == "":
            continue
        values = c.strip()[1:-1].split('","')
        clean = []
        for v in values:
            v = v.strip()
            if v == "":
                v = "N/A"
                
            clean.append(v)
        rows.append(clean)
    return rows, header

def main():
    
    rows, header = customer_info_clean()
    
    i = 0
    while i < len(header):
        print("|", header[i], end=" | ")
        i+=1
    print()
    print(rows[0][4], rows[0][5], rows[0][6], rows[0][8], rows[0][7])
    
    print("Press '1' to sort by Company Name")
    print("Press '2' to sort by Contact Name")
    print("Press '3' to search by Company Name")
    print("Press '4' to search by Contact Name")
    
    while True:
            
        q = input("What would you like to do?: ")
        if q in ['1', '2']:
            rows_sorting(rows, header, q)
        elif q in ['3', '4']:
            rows_search(rows, header, q)
        elif q in ["q", "Q", "Quit", "QUIT"]:
            break
        else:
            print("Please make a valid selection (Q to quit): ")
            
    
main()