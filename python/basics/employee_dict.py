employees=[{
    "name":"Enzo",
    "hours":45,
    "hourly_pay":18.50,
    "age":41
},
{
     "name":"Chiara",
     "hours":40,
     "hourly_pay":16.50,
     "age":26
},
{
     "name":"Martyna",
     "hours":35,
     "hourly_pay":13.50,
     "age":21
}]
### add salary for employee Chiara in the dict##
#salary=employees[1]["hours"]*employees[1]["hourly_pay"]
#employees[1]["salary"]=f"£ {salary}"
#print(employees[1]["name"])
#print(employees[1]["hours"])
#print(f"£ {salary}")
#print(employees)


#add salary for each employee and total salary to pay
total_salary=0
for employee in employees:
    salary=employee["hours"]*employee["hourly_pay"]
    total_salary=total_salary+salary
    print(f"{employee["name"]},{employee["hours"]} hours, £ {salary}")
print(f"Total salary to pay :£ {total_salary}")