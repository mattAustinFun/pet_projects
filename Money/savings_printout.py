# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 09:53:56 2025

@author: matth
"""
def saving_annual_summary( 
        monthly_saving: float, 
        interest_rate: float,
        initial_savings: float = 0)->str:
    """ Provide annual projection of savings based on monthly saving amount. """

    interest_month_rate = (interest_rate/100)/12
    interest_month_value = 0 
    interest_total_value = 0
    savings_added = 0
    savings_total = initial_savings
    saving_summary = "Month|Interest|Interest Total|Saving Added|Saving Total\n"
    saving_line = ""
    for month in range(1,13):
        interest_month = interest_month_rate * savings_total
        interest_total_value += interest_month
        savings_total += (interest_month + monthly_saving)
        savings_added = savings_total - initial_savings
        if (month % 3) == 0:
            saving_line = (
            f"{str(month).rjust(5)}|"
            f"{str(round(interest_month,2)).rjust(8)}|"
            f"{str(round(interest_total_value,2)).rjust(14)}|"
            f"{str(round(savings_added,2)).rjust(12)}|"
            f"{str(round(savings_total,2)).rjust(12)}\n")
            #print(saving_line)
            saving_summary += saving_line
    return saving_summary
    
print(saving_annual_summary(400.00,4.01,12000.00))