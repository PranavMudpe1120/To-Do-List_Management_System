MY TO-DO LIST
================

A simple console-based To-Do List application built with Python. The program allows users to view tasks, add new tasks with deadlines, remove tasks, and exit the application.


1. PROJECT OVERVIEW
===================

The My To-Do List project is a beginner-friendly command-line application designed to help users manage a small list of tasks.

Tasks are stored in memory using a Python list. Each task is represented by a dictionary containing:

- name — the task name
- deadline — the task deadline in DD/MM/YYYY format

The application provides a menu-driven interface so that users can select the operation they want to perform.

Note: The current version stores tasks only while the program is running. Closing the program removes all stored tasks because no permanent database or file storage is implemented.


2. PROBLEM STATEMENT
====================

People often need a simple way to keep track of tasks and their deadlines. This project provides a basic command-line solution where users can add, view, and remove tasks from a to-do list.


3. OBJECTIVES
=============

The main objectives of this project are:

1. Create a simple task-management application using Python.
2. Allow users to add tasks along with deadlines.
3. Display all currently stored tasks.
4. Allow users to remove a selected task.
5. Provide a clear and logical menu-driven workflow.
6. Apply Python concepts such as lists, dictionaries, loops, conditional statements, user input, and data structures.


4. FEATURES
===========

4.1 View Tasks
--------------
Displays all tasks currently stored in the to-do list, including their task number, name, and deadline.

If there are no tasks, the application displays:

No tasks yet!


4.2 Add Task
------------
Allows the user to enter:

- Task name
- Deadline in DD/MM/YYYY format

The task is then added to the list.


4.3 Remove Task
---------------
Displays the available tasks and allows the user to enter the number of the task they want to remove.

The selected task is removed from the list.


4.4 Exit
--------
Ends the program and displays a goodbye message.


5. FUNCTIONAL REQUIREMENTS
==========================

1. View Tasks:
   Display all tasks and their deadlines.

2. Add Task:
   Accept a task name and deadline and store the task.

3. Remove Task:
   Remove a task using its task number.

4. Exit:
   Terminate the application.

5. Input Selection:
   Allow the user to choose an operation from the menu.


6. NON-FUNCTIONAL REQUIREMENTS
=============================

Usability:
The application uses a simple numbered menu that is easy to understand and operate.

Maintainability:
The code uses meaningful variable names such as tasks, task_name, due_date, and choice.

Reliability:
The application checks whether the task list is empty before viewing or removing tasks and checks whether a selected task number is within the valid range.

Resource Efficiency:
The application uses a simple in-memory Python list and dictionaries, requiring minimal system resources for a small number of tasks.

Error Handling:
The application handles invalid menu choices and invalid task numbers. The current implementation does not yet handle non-numeric input for the task-removal number.


7. TECHNOLOGIES USED
====================

- Programming Language: Python 3
- Data Structures: List and Dictionary
- Interface: Command-Line Interface (CLI)
- Storage: In-memory storage

No external Python libraries are required for the current implementation.


8. HOW THE APPLICATION WORKS
============================

The application follows this workflow:

Start
  |
  v
Display Main Menu
  |
  +----> 1. View Tasks ----> Display Tasks
  |
  +----> 2. Add Task ------> Enter Name & Deadline
  |                              |
  |                              v
  |                         Store Task
  |
  +----> 3. Remove Task ---> Select Task Number
  |                              |
  |                              v
  |                         Remove Task
  |
  +----> 4. Exit ----------> End Program
  |
  v
Return to Main Menu


9. PROJECT STRUCTURE
====================

The current implementation can be organized as:

my-todo-list/
|
|-- todo_list.py
|-- README.md

The current version is a simple single-file implementation. For a larger academic project, the code can later be divided into multiple modules.


10. INSTALLATION AND SETUP
==========================

Prerequisites:

Install Python 3 on your computer.

Check whether Python is installed:

python --version

or:

python3 --version

Setup:

1. Create a project folder.
2. Save the Python program as todo_list.py.
3. Save this README as README.md.
4. Open a terminal in the project folder.


11. RUNNING THE PROJECT
=======================

Run the program with:

python todo_list.py

If your system uses python3, run:

python3 todo_list.py

The application will display:

==== MY TO-DO LIST ====
1. View Tasks
2. Add Task
3. Remove Task
4. Exit
Choose an option:


12. USAGE
=========

Add a Task:

Select option 2:

Choose an option: 2
Enter task name: Complete Python project
Enter deadline (DD/MM/YYYY): 30/09/2026
Task added!


View Tasks:

Select option 1:

Choose an option: 1

My Tasks:
1 - Complete Python project | Deadline: 30/09/2026


Remove a Task:

Select option 3:

Choose an option: 3

Tasks:
1 - Complete Python project
Which task do you want to remove? 1
Removed: Complete Python project


Exit:

Select option 4:

Choose an option: 4
Bye!


13. DATA STORAGE
================

The current application uses an in-memory list:

tasks = []

Each task is stored as a dictionary:

task = {
    "name": task_name,
    "deadline": due_date
}

For example:

[
    {
        "name": "Complete Python project",
        "deadline": "30/09/2026"
    }
]

There is currently no database or permanent file storage.


14. TESTING
===========

The current project can be manually tested using the following cases:

Test Case 1:
Action: Select 1 before adding tasks.
Expected Result: "No tasks yet!"

Test Case 2:
Action: Select 2 and enter valid task details.
Expected Result: Task is added.

Test Case 3:
Action: Select 1 after adding a task.
Expected Result: Task and deadline are displayed.

Test Case 4:
Action: Select 3 and enter a valid task number.
Expected Result: Selected task is removed.

Test Case 5:
Action: Enter a number outside the task range.
Expected Result: "Invalid task number."

Test Case 6:
Action: Select 3 when the list is empty.
Expected Result: "Nothing to remove."

Test Case 7:
Action: Enter an option other than 1, 2, 3, or 4.
Expected Result: Prompt to enter a valid option.

Test Case 8:
Action: Select 4.
Expected Result: Program terminates.

The current project does not contain an automated unit-test suite.

15. VITYARTHI PROJECT ALIGNMENT
===============================

The VITyarthi project guidelines require students to identify a meaningful problem, design a technical solution, implement the solution using concepts learned in the course, and demonstrate understanding through documentation and evaluation.

The guidelines also require functional requirements, non-functional requirements, appropriate documentation, testing where applicable, and a GitHub repository containing a README.md, statement.md, and organized project files.

This README covers the main repository documentation for the current To-Do List project.

For a stronger final submission, the project can be expanded with system architecture, workflow diagrams, UML diagrams, testing documentation, and a more modular implementation.


16. CONCLUSION
==============

My To-Do List is a simple Python command-line project that demonstrates basic task management using lists, dictionaries, loops, conditional statements, and user input.

The current version provides the essential operations needed for a basic to-do list while leaving room for additional features and a more modular architecture in future versions.
