
# ====== a program for a small business that can help it to manage tasks assigned to each member of the team ====== #

from datetime import date


login_info = [] # List to store user's login details

with open('user.txt', 'r') as f:
    for word in f.readlines():
        user, password = word.split(sep=", ") # defines user and password from txt file, notes that they are separated by ','
        login_info.append((user.strip(), password.strip())) # Adds user's details to login_info list

while True:
    username = str(input('Please input your username: '))
    userpass = str(input('Please input your password: '))

    if (username, userpass) in login_info:
        print('Login Successful')
        break

    else:
        print('Details incorrect, please try again. Please note - username and password are case sensitive')

        f.close()

while True:

    # This block shows a new menu that only the admin has access to, that will show the total number of users and tasks
    if username == 'admin': # check user = admin
        stats_menu = input('Would you like to display current statistics? Y/N: ') 
        if stats_menu.lower() == 'y':
            num_tasks = 0 # counters to add user & task counts
            num_users = 0
            with open('tasks.txt', 'r') as f: # file opens
                for line in f: # file is read line by line
                    num_tasks += 1 # number of tasks added to counter
                print("_"*80 +"\n")
                print(f"\nTotal number of tasks: {num_tasks}") # items neatly printed with as strings with line separators
                

            with open('user.txt', 'r') as f2: # same as previous block, counting number of users
                for line in f2:
                    num_users += 1
                
                print(f"\nTotal number of users: {num_users}")
                print("_"*80 +"\n")


    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

    # Block to set 'Registering a user' to admin only, registers a new user and adds the details to the list of users in user.txt

    if menu == 'r':
        if username == 'admin':
            new_user = input('Please enter username: ')
            new_pass = input('Please enter a password: ')
            pass_check = input('Please confirm your password: ')
            if new_pass == pass_check:
                file = open('user.txt', 'a')
                file.write("\n" + new_user + ",")
                file.write(" " + new_pass)

                file.close()
                print('Registration complete')
                break
            else:
                print('Passwords do not match - Please try again')
        else:
            print('You are not authorised to add new users. Please contact your system administrator.') # block any user that is not 'admin' from adding new users
        

    #  Block that will allow a user to add a new task to task.txt file
  

    elif menu == 'a':
        today = date.today() # Gets today's date and stores in 'today' variable
        user = str(input('Please input the username of the person assigned to this task: ')) # user inputs the name of the person assigned to the task
        title = str(input('What is the title of this task? '))
        description = str(input('Please enter a brief description of the task: '))
        due_date = str(input('When is the task due to be completed? '))
        todays_date = today.strftime("%A %d %B %Y")

        f = open('tasks.txt', 'a')
        f.write("\n" + user + ", " + title + ", " + description + ", " + due_date + ", "  + todays_date + ", " + 'No') # adds all info to the tesxt file with 'No' top signify that the task has no yet been completed
        f.close()
        print('Task added') # Prints confirmation for the user

   
    # Block to read the tasks from task.txt file and neatly print to the console

    elif menu == 'va':

        info = []

        with open('tasks.txt', 'r') as f: # file opens
            for word in f.readlines(): # file is read line by line
                assigned_to, task_title, task_desc, due, date_assigned, completed = word.split(sep=",") # variables added to information in tasks.txt word by word - split by ','
                info.append((assigned_to.strip(), task_title.strip(), task_desc.strip(), due.strip(), date_assigned.strip(), completed.strip())) # stripped items added to a list
                print("_"*80 +"\n")
                print("Task: " + str(task_title) +"\nAssigned to: " + str(assigned_to) +"\nDate Assigned: " + str(date_assigned) +"\nDue Date: " + str(due) +"\nTask Complete? " + str(completed) +"\nTask Description:  " + str(task_desc)) # items neatly printed with as strings with line separators
                print("_"*80 +"\n")


    # Block to print that specific user's current tasks

    elif menu == 'vm':

        user = []

        with open('tasks.txt', 'r') as f: # file opens
            for word in f.readlines(): # file is read line by line
                assigned_to, task_title, task_desc, due, date_assigned, completed = word.split(sep=",") # variables added to information in tasks.txt word by word - split by ','
                user.append((assigned_to.strip(), task_title.strip(), task_desc.strip(), due.strip(), date_assigned.strip(), completed.strip())) # # stripped items added to a list
                if username == assigned_to: # checks which user is logged in and checks the file for that user, then prints only that user's tasks
                    print("_"*80 +"\n")
                    print("Task: " + str(task_title) +"\nAssigned to: " + str(assigned_to) +"\nDate Assigned: " + str(date_assigned) +"\nDue Date: " + str(due) +"\nTask Complete? " + str(completed) +"\nTask Description:  " + str(task_desc))
                    print("_"*80 +"\n")

        if username != assigned_to:
            print('You have no more tasks\n')


    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")