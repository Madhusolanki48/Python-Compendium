# bill_total function

def bill_total(bill):
    total=0.00
    for k,v in bill.items():
        total+=v
        return total
    
# calculate_tax function

def calculate_tax(percent,bill_total):
    return round((percent*bill_total)/100.0,2)

Food_bill={
    'juice':3.99,
    'breadsticks':4.55,
    'salad':11.99,
    'chicken':22.00,
    'tea':2.00
}

# calculate_tax function

food_total=bill_total(Food_bill)
tax_total=calculate_tax(15,food_total)
print("Total: ",food_total)
print("Tax: ",tax_total)
print("Overall: ",food_total+tax_total)

