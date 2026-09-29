name=input("Please enter your name : ")
hourly_rate= float(input("Please enter hourly rate : "))
daily_hours=8
weekly_day=5
day=0
for i in range(5):
    day=day+1
    sal=daily_hours*hourly_rate
    salary=(f"Day: {day} salary : £ {sal}")
    print(salary)
    total_salary=sal*weekly_day
print(f"Weekly salary : £ {total_salary}")
    
