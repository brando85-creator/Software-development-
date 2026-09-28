name= input("Please enter your name:  ")
age = input("Please enter your age:  ")
Hourly_pay= float(input("Please enter your hourly pay:  "))
weekly_hours= int(input("Please enter your weekly hours:  "))
if weekly_hours > 40:
    extra= weekly_hours -40
    extra_earn= extra*Hourly_pay*1.5
salary= weekly_hours* Hourly_pay
net_salary= salary-(salary*20/100)
print(f"{name} is {age} years old")
print(f"{name}) worked for {weekly_hours}")
print(f"{name} salary for last week is £{net_salary} with extra of {extra_earn}")