'''
# Part A

total_cost = 0# the cost of my dream house
portion_down_payment = 0.25#portion of the cost needed for a down payment
current_savings = 0
r = 0.04
annual_salary = 0
portion_saved = 0#amount of your salary each month to saving for the down payment
# monthly salary = 0

months = 0

#Enter info
annual_salary = int(input("Enter your annual salary: ").strip())
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:  ").strip())
total_cost = int(input("Enter the cost of your dream home: ").strip())

# Caculate
while current_savings < total_cost * portion_down_payment:
    current_savings += annual_salary/12*portion_saved + current_savings*r/12
    months += 1

print("Number of months: ",months)
'''
'''
# Part B

total_cost = 0# the cost of my dream house
portion_down_payment = 0.25#portion of the cost needed for a down payment
current_savings = 0
r = 0.04
annual_salary = 0
portion_saved = 0#amount of your salary each month to saving for the down payment
# monthly salary = 0

months = 0

semi_annual_raise = 0 #new: salary raise

#Enter info
annual_salary = int(input("Enter your annual salary: ").strip())
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:  ").strip())
total_cost = int(input("Enter the cost of your dream home: ").strip())

semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal: ").strip())

# Caculate
while current_savings < total_cost * portion_down_payment:
    if months % 6 == 0 and months != 0:
        annual_salary += annual_salary * semi_annual_raise
    current_savings += annual_salary/12*portion_saved + current_savings*r/12
    months += 1

print("Number of months: ",months)
'''

# Part C

total_cost = 1000000# certain
portion_down_payment = 0.25#portion of the cost needed for a down payment
current_savings = 0
r = 0.04
annual_salary = 0
portion_saved = 0.5#initially half
# monthly salary = 0

months = 0

semi_annual_raise = 0.07 #salary raise

steps = 0

#bisection search (tips by AI)
min_ = 0
max_ = 1
mid = (min_ + max_)/2

#Enter info
annual_salary = int(input("Enter your annual salary: ").strip())
temp_ = annual_salary

# impossible case
while current_savings < total_cost * portion_down_payment:
    if months % 6 == 0 and months != 0:
        annual_salary += annual_salary * semi_annual_raise
    current_savings += annual_salary/12 + current_savings*r/12
    months += 1
    
current_savings = 0

if months > 36:
    print("impossible")
else:
    annual_salary = temp_
    current_savings = 0
    months = 0
    min_ = 0.0
    max_ = 1.0
    steps = 0
    
    while max_ - min_ > 0.0001:
        mid = (max_ + min_)/2
        
        annual_salary = temp_
        current_savings = 0
        months = 0
        
        while months < 36 and current_savings < total_cost * portion_down_payment:
            if months % 6 == 0 and months != 0:
                annual_salary += annual_salary * semi_annual_raise
            current_savings += annual_salary/12*mid + current_savings*r/12
            months += 1
        
        if current_savings >= total_cost * portion_down_payment:
            max_ = mid
        else:
            min_ = mid
        
        steps+=1
    
    mid = (max_+min_)/2
    print("Best savings rate: ",mid)
    print("Steps in bisection search: ",steps)



