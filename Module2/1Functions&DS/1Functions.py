bill=175.00
tax_rate=15
total_tax=(bill*tax_rate)/100.00
print('Total tax',total_tax)

# Using Function
def calculate_tax(bill2,tax_rate2):
    return(bill2*tax_rate2)/100.00
print('Total Tax: ',calculate_tax(175.00,15))
print('Total Tax: ',calculate_tax(193.00,25))