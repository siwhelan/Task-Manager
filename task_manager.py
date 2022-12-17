
# ====== a program for a small business that can help it to manage tasks assigned to each member of the team ====== #

from datetime import date
from datetime import datetime


# ====== Functions to be called later, depending on user input ====== #



# Function to allow the admin to register a new user, checking that each new username is not already in use #

# The function also asks the new user to confirm their password and, if they match, adds new user login details to a text file # 

def reg_user(user_input):

    if user_input.lower() == "r":

        # Checks that the user has admin priveleges

        if username == 'admin':
            new_user = str(input('Please enter username: \n'))

            
            with open('user.txt', 'r') as f:

                usernames = f.read()

                # Check to make sure the username isn't already in use, prompt for a new username if it is

                while new_user in usernames:
                    
                    new_user = str(input('Username already in use, please try a different name: \n'))
                    continue


                # If the new username is accepted, asks for a new password

                if new_user not in usernames:

                    # Stores the password in new_pass, asks user to confirm password
                                        
                    new_pass = str(input('Please input your password: \n'))
                    pass_check = str(input('Please confirm your password: \n'))
                    
                

            # Checks password & confirmation match

            if new_pass == pass_check:
                    
                # Writes the info to the txt file

                file = open('user.txt', 'a')
                file.write("\n" + new_user + ",")
                file.write(" " + new_pass)
                file.close()

                print('Registration complete')
                
            
            # Errors occur if passwords do not match or user does not have admin privelegs

            else:
                print('Passwords do not match - Please try again')
        else:
            print('You are not authorised to add new users. Please contact your system administrator.')
    
# Function to allow the user to add a new task #

def add_task(user_input):

    if user_input.lower() == 'a':

        from datetime import datetime
        from datetime import date

        today = date.today()

        # Fetches today's date and stores in 'today' variable

        # user inputs all relevant task info as requested. Info is stored in multiple variables. Task completed is 'No' as default

        user = str(input('Please input the username of the person assigned to this task: '))
        title = str(input('What is the title of this task? '))
        description = str(input('Please enter a brief description of the task: '))
        due_date = str(input('When is the task due to be completed? e.g 21 Oct 2022: '))
        date_assigned = today.strftime('%d %b %Y')
        task_completed = 'No'

        # Appends new task and all info to the text file and store data in a list and a dictionary for later use.


        with open('tasks.txt', 'a+') as f:
            
            f.write("\n" + user + ", " + title + ", " + description + ", " + due_date + ", "  + date_assigned + ", " + task_completed)
            
            #f.write(f"\n{task_list}")

            print('Task added')

# Function to show all tasks upon user request #

def view_all(user_input):

    if user_input.lower() == 'va':

        # Empty list to store data

        info = []
        task_count = 0

        with open('tasks.txt', 'r') as f:
            for word in f.readlines():

                # Task details assigned to individual variables, along with a counter

                task_count += 1
                assigned_to, task_title, task_desc, due, date_assigned, completed = word.split(sep=",")

                # Stripped task added to the info list and neatly printed to the terminal

                info.append((assigned_to.strip(), task_title.strip(), task_desc.strip(), due.strip(), date_assigned.strip(), completed.strip())) 
                print("_"*80 +"\n")
                print("Task " + str(task_count) + ":" + str(task_title) +"\nAssigned to: " + str(assigned_to) +"\nDate Assigned: " + str(date_assigned) +"\nDue Date: " + str(due) +"\nTask Complete? " + str(completed) +"\nTask Description:  " + str(task_desc))
                print("_"*80 +"\n")

# Function to show the user their own tasks #

def view_mine(user_input):


    if user_input.lower() == 'vm':

        # Empty lists to add user specific task details 
        # Counter to number tasks

        user = []
        task_count = 0
        task_list = []
        edit_task = []

        # file opens

        with open('tasks.txt', 'r') as f:

            # file is read line by line

            for word in f.readlines(): 
                task_count += 1

                # variables added to information in tasks.txt word by word - split by ','

                assigned_to, task_title, task_desc, due, date_assigned, completed = word.split(sep=",")

                # stripped task added to a list

                user.append((assigned_to.strip(), task_title.strip(), task_desc.strip(), due.strip(), date_assigned.strip(), completed.strip()))

                # checks which user is logged in and checks the file for that user, then prints only that user's tasks

                if username == assigned_to: 
                    print("_"*80 +"\n")
                    print("Task " + str(task_count) + ":" + str(task_title) +"\nAssigned to: " + str(assigned_to) +"\nDate Assigned: " + str(date_assigned) +"\nDue Date: " + str(due) +"\nTask Complete? " + str(completed) +"\nTask Description:  " + str(task_desc))
                    print("_"*80 +"\n")

            if username != assigned_to:
                print('You have no more tasks\n')

        # Saving full tasks file into a list

        task_list = []
        for line in open('tasks.txt'):
            task = line.rstrip('\r\n').split('\t') # strip new-line characters
            task = [item.strip() for item in task] # strip whitespace, save to lists
            task_list.append(task) # Append each task into the task_list list

        # print(task_list)

        # Allow user to enter a number referring to the task they'd like to edit, or -1 to return to the main menu

        task_select = int(input('Please enter a task number to edit, or type "-1" to return to the main menu: '))

        if task_select == -1:

            return

        else:
            
            # save the specified task into a variable 

            edit_task = task_list[task_select-1]

            # Print confirmation

            print(edit_task)

        complete = str(input('Would you like to mark this task as complete? Y/N: '))

        # If the task is to be marked as complete, pull that task into a temporary list, with each detail (name, due dat, task description etc) as items in the list

        if complete.lower() == 'y':
            
            temp_list = []
            for item in edit_task:
                item = item.split(',')
                temp_list.extend(item)
            # print(temp_list)

            # Change the relevant index, in this case [5] to 'Yes' to mark the task complete

            temp_list[5] = 'Yes'

            print('The task has been marked as complete.')

            # Add the updated task back into the temp_list, replacing the old 'incomplete' version

            task_list[task_select-1] = temp_list

            # print(task_list)

            # Write the updated task list back to the text file

            with open('tasks.txt', 'w') as f:
                
                for item in task_list:
                    f.write(",".join(map(str,item)))
                    f.write("\n")


        elif complete.lower() == 'n':

            # Same list as before, this time to allow further options if the task is not completed

            temp_list = []
            for item in edit_task:
                item = item.split(',')
                temp_list.extend(item)

            # print(temp_list[5])

            # If the task has not been completed

            if temp_list[5] == ' No':

                # Ask the user if they'd like to edit a particular detail

                edit_select = input('Would you like to edit the user assigned to this task or the due date? Please enter "new" or "due": ')

                if edit_select.lower() == 'new':

                    # If the user wishes to edit the task, ask them to input the reassigned user's name

                    new_user = str(input('Please enter the name of the user you wish to reassign the task to: '))

                    # Check that user exists

                    if new_user in username_list:

                        # Update the list with the new details and write back to the file

                        temp_list[0] = new_user

                        print('The user assigned to this task has been updated.')

                        task_list[task_select-1] = temp_list

                        with open('tasks.txt', 'w') as f:
                
                            for item in task_list:
                                f.write(", ".join(map(str,item)))
                                f.write("\n")

                    # Error messgae if the reassigned user does not exist

                    else:
                        print('User not recognised, please try again')
                        return

                elif edit_select.lower() == 'due':

                    # Ask for a new due date in the correct format

                    new_date = input('Please enter a new due date, e.g 21 Dec 2022: ')

                    # Same process as above, changing due date this time

                    temp_list[3] = new_date

                    print('The due date of this task has been updated.')

                    task_list[task_select-1] = temp_list

                    with open('tasks.txt', 'w') as f:
            
                        for item in task_list:
                            f.write(", ".join(map(str,item)))
                            f.write("\n")        


            # Error if the user tries to update a task that has already been completed

            else:
                print('You can only edit uncompleted tasks')
                return


# Function to view basic stats #

def view_stats(user_input):

    if user_input.lower() == 'vs':

        # Call generate reports in case the task and user overview files do not exist

        # Print content of the reports to the terminal

        print(generate_reports())

        print("_"*80 +"\n")

        with open('task_overview.txt', 'r') as f: 
            for line in f: 
                print(line) 

        print("_"*80 +"\n")
            
           
        print("_"*80 +"\n")

        with open('user_overview.txt', 'r') as f2:
            for line in f2:
                print(line)
        
        print("_"*80 +"\n")

# Function to generate detailed reports and write them to a text file #

def generate_reports():


    num_tasks = 0 # counters to add user & task counts
    num_users = 0
    with open('tasks.txt', 'r') as f: # file opens
        for line in f: # file is read line by line
            num_tasks += 1 # number of tasks added to counter

    with open('user.txt', 'r') as f2: # same as previous block, counting number of users
        for line in f2:
            num_users += 1

    completed_count = 0
    not_completed_count = 0
    with open('tasks.txt', 'r') as f3:
        for line in f3:
            if ' Yes' in line:
                completed_count += 1
            elif ' Yes' not in line:
                not_completed_count += 1
        # print(not_completed_count)


    with open('tasks.txt', 'r') as f4:

        count = 0
        overdue_count = 0
        num_tasks = 0
        not_completed_count = 0

        for line in f4:

            newline = line.rstrip('\n')  # Stripping newline characters.
            
            task_list = newline.split(", ")  # Splitting line into a list of items.

            num_tasks += 1


            today = datetime.today()
            due_date = task_list[3]
            completed = task_list[5]
            due = datetime.strptime(due_date, '%d %b %Y')
            # print(due)

            if due < today and completed == 'No':
                count += 1
                overdue_count += 1

            if completed == 'No':
                not_completed_count += 1
        
            
            incomplete = round((not_completed_count / num_tasks) * 100, 2)
            overdue = round((overdue_count / num_tasks) * 100, 2)
        
        # print(overdue_count)

    file = open('task_overview.txt', 'w')

    file.write(

        f'Total number of tasks: {num_tasks}\n'
        f'Total completed tasks: {completed_count}\n'
        f'Total uncompleted tasks: {not_completed_count}\n'
        f'Total uncompleted & overdue tasks: {count}\n'
        f'Percentage of tasks incomplete: {incomplete}%\n'
        f'Percentage of tasks overdue: {overdue}%\n'

    )

    with open('tasks.txt', 'r') as f5:
        
        
        my_tasks = 0
        my_complete_tasks = 0
        my_incomplete_tasks = 0
        my_overdue = 0

        for line in f5:

            newline = line.rstrip('\n')  # Stripping newline characters.
            
            task_list = newline.split(", ")  # Splitting line into a list of items.

        
            if str(task_list[0]) == username:
                my_tasks += 1

            if str(task_list[5]) == 'Yes':
                my_complete_tasks += 1
            elif str(task_list[5]) == 'No':
                my_incomplete_tasks += 1

            today = datetime.today()
            due_date = task_list[3]
            completed = task_list[5]
            due = datetime.strptime(due_date, '%d %b %Y')
            # print(due)

            if due < today and completed == 'No':
                count += 1
                my_overdue += 1


        # print(my_tasks)

        my_percentage = round((my_tasks / num_tasks) * 100, 2)
        my_percentage_comp = round((my_tasks / my_complete_tasks) * 100, 2)
        my_percentage_incomp = round((my_incomplete_tasks / my_tasks) * 100, 2)
        overdue = round((my_overdue / my_tasks) * 100, 2)
        



    file2 = open('user_overview.txt', 'w')

    file2.write(

        f'Total number of users: {num_users}\n'
        f'Total number of tasks: {num_tasks}\n'
        f'Number of tasks assigned to you: {my_tasks}\n'
        f'Percentage of tasks assigned to you: {my_percentage}\n'
        f'Percentage of tasks assigned to you that are complete: {my_percentage_comp}\n'
        f'Percentage of tasks assigned to you that are not complete: {my_percentage_incomp}\n'
        f'Percentage of tasks assigned to you that are not complete and are now overdue: {overdue}\n'

    )


    print('\nReports generated succesfully')




# ====== Task Manager Program ====== #



# Empty Lists/Dicts to store user's login and task details

from datetime import datetime

username_list = []
password_list = []

login_info = {}

task_list = []

count = 1


# Opens text file, reads data and stores username and passwords in two lists, split by ','

with open('user.txt', 'r') as f:
    for word in f.readlines():
        user, password = word.split(sep = ", ")         
        username_list.append(user.strip())                        
        password_list.append(password.strip())
    
        # Store names and passwords in a dictionary as {User:Password} to check login details are correct for each user

        login_info = dict(zip(username_list, password_list))




# ====== Login Section ====== #


while True:

    # Asks user to enter their login details 

    username = str(input('Please input your username: \n'))
    userpass = str(input('Please input your password: \n'))
    

    # Check if the entered username matches it's corresponding password in login_info
    # If details are incorrect, give an error message

    if login_info.get(username) == userpass:
        print('\nLogin Successful.')
        break

    else:
        print('\nDetails incorrect, please try again. Please note - username and password are case sensitive')

while True:

    # This block shows a new menu with extra featurews that only the admin has access to

    if username == 'admin': # check user = admin

            menu = input('''\nSelect one of the following user_choices below:

r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - generate reports
vs - view task statistics
e - Exit

: ''').lower()
       
            # Display total number of tasks and users

            if menu.lower() == 'vs':

                view_stats(menu)
                
            # Block to generate and print reports

            elif menu =='gr':

                generate_reports()

            # Choosing user_choice 'r' calls reg_user()
            
            elif menu == 'r': 

                reg_user(menu)
        

            #  Block that will allow a user to add a new task to task.txt file
  

            elif menu == 'a':

                add_task(menu)

    
            # Block to read the tasks from task.txt file and neatly print to the console

            elif menu == 'va':

                view_all(menu)

            # Block to print that specific user's current tasks

            elif menu == 'vm':

                view_mine(menu)


            elif menu == 'e':
                print('Goodbye!!!')
                exit()

            else:
                print("You have made a wrong choice, Please Try again")


    else:
        
        menu = input('''\nSelect one of the following user_choices below:

r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - generate reports
e - Exit
: ''').lower()


        if menu == 'r': # Choosing user_choice 'r' calls reg_user()

            reg_user(menu)
        

    #  Block that will allow a user to add a new task to task.txt file
  

        elif menu == 'a':

            add_task(menu)

   
    # Block to read the tasks from task.txt file and neatly print to the console

        elif menu == 'va':

            view_all(menu)

    # Block to print that specific user's current tasks

        elif menu == 'vm':

            view_mine(menu)

    # Block to generate detailed reports and print info to relevant text files

        elif menu =='gr':

                generate_reports()

        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        else:
            print("You have made a wrong choice, Please Try again")
