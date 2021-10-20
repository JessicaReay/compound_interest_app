# App: compound interest calculator
# Fuction: calculates monthly compound interest for custom user inputs
# Author: Dan & Jess

def monthly_compounding(initial, monthly, years, annual_rate):
    sum = initial
    months = years *12 
    #iterate through months
    for month in range(int(months)):
        # apply annual rate to current balance
        sum = sum * (1+ annual_rate/ 1200)
        #ass monthly contribution 
        sum = sum + monthly
    return sum 
     
    #return initial + (monthly * 12 * years * (1+ annual_rate/100))