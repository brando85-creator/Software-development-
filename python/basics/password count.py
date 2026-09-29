print("------MAIN MENU------")
password="python12345"
attempt=0
while attempt <3:
    user_choice=input("Please enter your password : ")
    if user_choice== password:
        print("Access granted")
        attempt=attempt+1
        print(f"Attempt: {attempt}")
        break
    else:
        attempt=attempt+1
        print("Sorry wrong password! Try it again......")
        print(f"Attempt: {attempt}")
    if attempt==3:
        print("Sorry,too many wrong password. Try it later.... ")

   
    

        
        
        
    
        

        