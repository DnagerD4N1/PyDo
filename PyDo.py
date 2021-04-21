import time as ti
print("Hello and welcome to PyDo! A To-Do Python Script.")
ti.sleep(2)
print("Let's get started!")
ti.sleep(1)
print("To use PyDo you will need to use a PyDo account.")
ti.sleep(0.5)
print("Are you creating a account? yes/no (Case-sentative)")
user_input_1 = input("")
if user_input_1 == "yes":
    print("Okay please first enter your email adress. This could be a work/school email or a personal email.")
    user_email = input("")
    ti.sleep(1)
    print("Okay your email has been saved. Now it's time for your password. Please make a password that is atleast 6 charaters long.")
    user_pass = int(input(""))
    if user_pass > 6:
        print("Your password has been saved in our database! :)")
    else:
        print("Your password is too short! Try again!")
        user_pass = input("")

if user_input_1 == "no":
    print("Okay, please enter your email adress.")
    user_email = input("")
    ti.sleep(1)
    print("Okay...")
    ti.sleep(1)
    print("Please enter your password.")
    user_pass = input("")
    
ti.sleep(2)
todo = []
print("Please enter your your task")
todo = input("")
print("To print all of your tasks type 'all'. ")
print("To print your login type 'login'. ")
user_input_2 = input("")

if user_input_2 == "all":
    print(todo)
if user_input_2 == "login":
    print("Your email is: " + user_email + " .")
    print("Your password is: " + user_pass + " .")