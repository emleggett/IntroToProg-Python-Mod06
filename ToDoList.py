# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# RRoot,1.1.2020,Created starter script
# ELeggett,11.22.2021,Added and debugged code
# ---------------------------------------------------------------------------- #

# Define Data ---------------------------------------------------------------- #
# Declare variables and constants
file_name_str = "ToDoFile.txt"  # The name of the data file
file_create = open(file_name_str, "a")  # Creates/opens companion .txt file
table_lst = []  # A list that acts as a 'table' of rows
choice_str = ""  # Captures the user option selection

# Process Data --------------------------------------------------------------- #
class Processor:
    """  Perform processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) being populated with data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # Clears current data
        file = open(file_name, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Task": task.strip(), "Priority": priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """ Adds inputted data (task, priority) to indicated list of dictionary rows

        :param task: (string) indicating task to be added:
        :param priority: (string) indicating task priority:
        :param list_of_rows: (list) being populated with data:
        :return: revised (list) of dictionary rows
        """
        row = {"Task": task.lower(), "Priority": priority.lower()}
        if priority.lower() == "high":  # Conditional loop confirming user inputs valid task priority.
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
        else:  # Returns user to menu if invalid priority set.
            input("Please choose a priority between low, medium, and high!")
        return list_of_rows

    @staticmethod
    def remove_data_from_list(remove_task, list_of_rows):
        """ Removes inputted data (task, priority) from indicated list of dictionary rows

        :param remove_task: (string) indicating task to be removed:
        :param list_of_rows: (list) being actioned by function:
        :return: revised (list) of dictionary rows
        """
        bln_flag = False
        int_row = 0
        for row in list_of_rows:
            task, priority = dict(row).values()
            if remove_task.lower() == task.lower():  # Loop confirming indicated task exists in To Do list.
                list_of_rows.remove(row)
                bln_flag = True
            int_row += 1
        if bln_flag == True:
            print("Task successfully removed from list!")
        else:
            input("Task not found. Press Enter to return to main menu.")
        return list_of_rows

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Writes indicated list of dictionary rows to .txt file

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) being populated with data:
        :return: (list) of dictionary rows
        """
        file = open(file_name, "w")  # Opens .txt file in 'write' mode
        for row in list_of_rows:
            file.write(row["Task"] + ", " + row["Priority"] + "\n")  # Saves list data row by row into .txt file
        file.close()  # Closes .txt file
        return list_of_rows

# Presentation (Input/Output) --------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def output_menu_tasks():
        """  Displays a menu of options to the user

        :return: none
        """
        print("""
        Menu of Options
        1) Add New Task
        2) Remove Existing Task
        3) Save List to File        
        4) Exit Program
        """)

    @staticmethod
    def input_menu_choice():
        """ Collects menu option from user

        :return: (string) representing selected menu option
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Adds an extra line for readability.
        return choice

    @staticmethod
    def output_current_tasks_in_list(list_of_rows):
        """ Displays current To Do list as a list of dictionary rows

        :param list_of_rows: (list) of rows being displayed
        :return: none
        """
        print("\n******* Here is your current To Do list: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("************************************************\n")

    @staticmethod
    def input_new_task_and_priority():
        """ Collects task and priority from user to add to list

        :return: (string) data to process to file
        """
        task = input("Enter a task to add to the list: ")
        priority = input("Assign a priority (high, medium, low): ")
        return task, priority

    @staticmethod
    def input_task_to_remove():
        """ Collects task from user to remove from list

        :return: (string) to process to file
        """
        remove_task = input("Enter a task to remove from your to do list: ")
        return remove_task

# Main Body of Script ------------------------------------------------------- #

# Step 1: Load data from ToDoFile.txt when the the program starts.
Processor.read_data_from_file(file_name_str, table_lst)

while (True):
    IO.output_current_tasks_in_list(table_lst)  # Step 2: Display current To Do list data.
    IO.output_menu_tasks()  # Step 3: Display a menu of choices to the user.
    choice_str = IO.input_menu_choice()  # Step 4: Request menu choice from user.
    # Step 5: Process user's menu choice.
    if choice_str.strip() == "1":  # Choice 1: Add new task to list.
        (task, priority) = IO.input_new_task_and_priority()
        Processor.add_data_to_list(task, priority, table_lst)
        continue  # Returns user to main menu.
    elif choice_str == "2":  # Choice 2: Remove an existing task from list.
        remove_task = IO.input_task_to_remove()
        Processor.remove_data_from_list(remove_task, table_lst)
        continue  # Returns user to main menu.
    elif choice_str == "3":  # Choice 3: Save current To Do list data to file.
        save_choice = input("Save current list to file? This can't be undone! (y/n): ")  # Warns user that list data will be overwritten.
        if save_choice.lower() == "y":  # Saves data to files if user inputs 'y'.
            Processor.write_data_to_file(file_name_str, table_lst)
            input("Data saved to file. Press Enter to return to program.")
        else:  # Returns user to main menu if 'y' is not inputted.
            input("Data not saved to file. Press Enter to return to program.")
        continue  # Returns user to main menu.
    elif choice_str == "4":  # Choice 4: Exit program.
        print("Exiting program. Goodbye!")
        break  # Removes user from program.
    else:
        input("Please choose an option between 1 and 4!")  # Returns user to main menu if invalid menu option is chosen.
