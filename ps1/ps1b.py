#!/Users/ironic/mitpython/bin/python

# house hunting - part b
# determine how long it takes to save enough money for down payment on a
# house given a few basic assumptions and a semi-annual raise

import sys

def main():
    # user enters:
    # salary
    annual_salary = float(input('Enter your annual salary: '))

    # percentage of monthly salary to save for down payment
    portion_saved = float(input(
        'Enter the percent of your salary to save, as a decimal: '))

    # house cost
    total_cost = float(input('Enter the cost of your dream home: '))

    # semi-annual raise
    semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal: '))

    # state variables
    portion_down_payment = 0.25
    current_savings = 0.0
    r = 0.04    # annual rate of return
    monthly_salary = annual_salary / 12
    monthly_salary_saved = monthly_salary * portion_saved

    # set the base values
    investment_return = 0.0
    number_of_months = 0

    # while current savings are less than amount needed for downpayment
    while current_savings < total_cost * portion_down_payment:
        # calc investment return of current savings, 
        # then add it and monthly salary saved to current savings
        investment_return = current_savings * r / 12
        current_savings += (investment_return + monthly_salary_saved)

        # increment number of months
        number_of_months += 1
        if number_of_months % 6 == 0:
            monthly_salary_saved *= (1 + semi_annual_raise)

    print('Number of months:', number_of_months)

if __name__ == '__main__':
    main()
