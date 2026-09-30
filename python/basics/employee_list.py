employee=["Luigi","Anna","Giovanna","Enzo","Francesco"]
hours=[40,44,36,18,26]
for name, hour in zip(employee,hours):
    if hour>= 40:
        print(f"{name} : {hour} hours and is full time")
    elif hour >=20 and hour <=39:
         print(f"{name} : {hour} hours and is part time")
    else:
         print(f"{name} : {hour} hours and is casual")

   