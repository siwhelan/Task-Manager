
# Task Manager

A Python program designed for a small business that can help it to manage tasks assigned to each member of the team.

This program will work with two text files, user.txt and tasks.txt. It will open each of the files that accompany this project and take note of the following

    -> The username of the person to whom the task is assigned.
    -> The title of the task.
    -> A description of the task.
    -> The date that the task was assigned to the user.
    -> The due date for the task.
    -> Either a ‘Yes’ or ‘No’ value that specifies if the task has been completed yet.

user.txt stores the username and password for each user that has permission to use the program.

There is a default Admin account with additional priveleges outlined in the options below.

The program allows the user to do the following -

-> Login - an error is displayed should the user input a username and/or password that is incorrect

-> Register a new user (note - only Admin can add new users). An error is printed should the new username already be in use.

-> Add a new task - The user inputs the name of the person that the task will be assigned to, the task name, a short description and the due date. Each new task is written to the task.txt file.

-> View all tasks, these are printed on screen in an easy to read format

-> View personal tasks - Again printed in a neat format.

-> The Admin account can produce text files containing reports on the current tasks in the system. Details include - 

    ▪ The total number of tasks that have been generated and tracked using the task manager
    ▪ The total number of completed tasks.
    ▪ The total number of uncompleted tasks.
    ▪ The total number of tasks that haven’t been completed and that are overdue.

    ▪ The total number of tasks assigned to that user.
    ▪ The percentage of the total number of tasks that have been assigned to that user
    ▪ The percentage of the tasks assigned to that user that have been completed
    ▪ The percentage of the tasks assigned to that user that must still be completed
    ▪ The percentage of the tasks assigned to that user that have not yet been completed and are overdue

The program will run continuously, taking prompts from user input until the exit function is called. Incorrect input is anticipated throughout, and erros/solutions are put in place to prevent crashes and guide the user to the correct approach.

## Screenshots

![App Screenshot 1](https://i.imgur.com/SgD8kIy.jpg)

![App Screenshot 2](https://i.imgur.com/MbvJRu9.jpg)

![App Screenshot 3](https://i.imgur.com/s3spFjo.jpg)

## Feedback

If you have any feedback, please reach out to simon@swhelan.dev



## Authors

- [@siwhelan](https://github.com/siwhelan)


