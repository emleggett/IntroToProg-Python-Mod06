# DEFINING AND CALLING FUNCTIONS IN PYTHON

IT FDN 110-A | Module 06 | Assignment 06 | November 23, 2021

## Objective
Describe the steps taken to create the Python script attached to this assignment.

## Introduction
This week our course content primarily focused on creating more complex scripts through defining and calling user-defined functions to process and write data back to a .txt file. Though the objective of this week’s program is the same as last week’s (i.e., creating and administering a simple To Do list file), employing functions not only required that we separate our code into smaller, more serviceable parts, but also required careful attention to arguments as well as local and global data types.

## Process Data
To begin, it was necessary to give the program some basic parameters to work with. There were only three variables that required some sort of activation prior to the program running (as the rest were defined and populated within): file_name_str, table_lst, and choice_str. I also created a simple variable file_create to open (and, if nonexistent, create) the program’s companion .txt file. This was accomplished with the following line of code early in the script:

```
file_create open(file_name_str, “a")
```
 
From there, the script moves on to define the four functions it will use to process data: read, add, remove, and write. Though read, remove, and write were simple enough, I added some basic limitations to the add function preventing the user from inputting an invalid task priority. This was accomplished by inserting a short conditional loop into the function confirming that the inputted priority matched the options provided (low, medium, or high). I made a few attempts to condense the more repetitive elements, but ultimately the following proved to be most consistent and accurate:

```
if priority.lower() == "high":
    list_of_rows.append(row)
    print("Task successfully added to list!")
    return task, priority
elif priority.lower() == "medium":
    list_of_rows.append(row)
    print("Task successfully added to list!")
    return task, priority
elif priority.lower() == "low":
    list_of_rows.append(row)
    print("Task successfully added to list!")
    return task, priority
else:
    input("Please choose a priority between low, medium, and high!")
```

## Define Inputs & Collect Outputs
Next, the IO - or Input/Output - class was created to display program outputs to (in this case, the menu and to do list itself) as well as collect necessary inputs from (menu selection, tasks to be added/removed) the user. Compared to the processing functions, these were much simpler in syntax and purpose: of the five IO functions, only one passes through an argument and two of five do not indicate a specific return (i.e., output). As these functions are primarily tasked with collecting and displaying data, they also did not necessitate the use of conditionals or loops; instead, they largely employed input and print to engage with the user and collect inputs.

## Call Functions
TEXT

## Validate Code
TEXT

## Lessons Learned
