name= input("Please enter your name:  ")
age = input("Please enter your age:  ")
Hourly_pay= float(input("Please enter your hourly pay:  "))
weekly_hours= int(input("Please enter your weekly hours:  "))
if weekly_hours > 40:
    extra= weekly_hours -40
    extra_earn= extra*Hourly_pay*1.5
else:
    extra_earn=0
if weekly_hours>= 40:
    empl="full time"
elif weekly_hours >= 20 and weekly_hours<=39:
    empl="part time"
elif weekly_hours >1 and weekly_hours<19:
    empl="casual"
else:
    empl="no hours"
        
salary= weekly_hours* Hourly_pay
net_salary= salary-(salary*20/100)
if net_salary >= 600:
    sal="hight salary"
elif net_salary >= 300:
    sal="medium salary"
else:
    sal="no worked"
print(f"{name} is {age} years old")
print(f"{name} worked for {weekly_hours}")
print(f"{name} salary for last week is £{net_salary} with extra of {extra_earn}, is a {sal} and is position is {empl}")