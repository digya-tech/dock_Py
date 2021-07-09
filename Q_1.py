"""Ramesh's basic salary is input through the keyboard. 
   His dearness allowance is 40% of basic salary, and house rent allowance is 20% of basic salary.
   Write a program to calculate his gross salary."""


#input
basic_salary = int(input(" What is your basic salary: "))

# dearness allowance
dr_allow = basic_salary*40/100
print("Ramesh'Dearness Allowance is : ", (dr_allow))

# rent allowance
rt_allow = basic_salary*20/100
print("Ramesh's Rnt Allowance is : ", (rt_allow))

#Gross Salary
Gross_salary = (basic_salary + dr_allow + rt_allow)
print("Gross Salary of Ramesh is : ", (Gross_salary))
