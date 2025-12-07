#!/Users/ironic/mitpython/bin/python

# house hunting - part c
# find the best savings rate to amass a 25% down payment on a $1M house
# within 36 months. user inputs salary
# use bisection search

import sys

def main():
    # user enters salary
    annual_salary = float(input('Enter your starting salary: '))

    # these are fixed for modeling
    savings_time_limit = 36
    total_cost = 1000000
    down_payment = int(total_cost * 0.25)
    semi_annual_raise = 0.07

    # state variables
    portion_saved = 0.0     # rate of savings needed to get dp in 36 mo
    r = 0.04                # annual rate of return

    # bisection limits
    mid = 0
    low = 0
    high = 10000
    epsilon = 100

    # set the base values
    investment_return = 0.0
    number_of_steps = 0
    interest_rate_conversion_factor = 10000
    current_savings = 0.0
    possible = True

    # run simulation, set/reset variables
    while abs(current_savings - down_payment) > epsilon:
        current_savings = 0.0
        monthly_salary = annual_salary / 12
        mid = int((low + high) / 2)
        portion_saved = mid / interest_rate_conversion_factor
        # we can't save more than we earn
        if portion_saved >= 0.9999:
            possible = False
            break

        # calculate amount saved during the savings time limit
        for m in range(savings_time_limit):
            monthly_salary_saved = monthly_salary * portion_saved

            # calc investment return of current savings, 
            # then add it and monthly salary saved to current savings
            investment_return = current_savings * r / 12
            current_savings += (investment_return + monthly_salary_saved)

            # do we apply the semi-annual bonus?
            if m > 0 and m % 6 == 0:
                monthly_salary *= (1 + semi_annual_raise)

        # compare current savings to down payment
        if current_savings < down_payment:
            low = mid
        else:
            high = mid

        #increment steps for next run
        number_of_steps += 1

    if possible:
        print('Best savings rate: {}'.format(round(portion_saved, 4)))
        print('Steps in bisection search:', number_of_steps)
    else:
        print('It is not possible to pay the down payment in three years')

if __name__ == '__main__':
    main()
