# Python_mesia

**Task 1: Dynamic Input and String Manipulation**

This repository contains a Python program that performs various string manipulation tasks based on dynamic input. The program reads a string statement from the command line and accomplishes the following tasks:

- Adds exception handling wherever necessary.
- Determines the total number of characters present in the statement.
- Calculates the total number of duplicate characters in the statement.
- Counts the total number of words present in the statement.
- Identifies the total number of duplicate words in the statement.
- Reverses the characters present in the statement.
- Reverses the words present in the statement.
- Forms a new statement from the reversed words.
- Removes duplicate characters from the latest statement.
- Prints the final latest string statement.

The program ensures that all inputs are dynamic, preventing the use of static input. Each task is uniquely implemented, and the program is designed to be explanatory through its code.

To run the program, follow these steps:
1. Clone this repository to your local machine using the following command:
git clone https://github.com/Maryterralogic/Python_mesia.git
2. Open a terminal or command prompt and navigate to the repository's directory:
cd Python_mesia
3. Add your Python file to the staging area:
git add string_function.py
4. Commit your changes:
git commit -m "Initial commit"
5. Push your changes to the remote repository's branch (replace `ramp_up_python_mesia` with the appropriate branch name):
git push origin ramp_up_python_mesia
6. Execute the Python program in the terminal, providing the required input as prompted:
python .\string_function.py

**Task 2:Email Validation:**

1.Clone the repository or copy the provided Python code into a .py file on your local machine.
2.Run the program using a Python interpreter:
  python pinging_ip_validation.py
3.The program will prompt you to enter an email address for validation.
4.If the email address is valid based on the regular expression, the program will store it in a file named email_list.txt.
5.The program will continue to prompt for email addresses until you choose to exit.
6.If you choose to exit by typing "No" or "exit", the program will display a list of email IDs stored in the file.
Features:
- Validates email addresses using a regular expression pattern.
- Stores valid email addresses in a file for later retrieval.
- Provides options to continue or exit the validation process.
- Displays a list of stored email IDs when the user decides to exit.

**Task3:IP Validation and Ping Check Program:**
  This Python program validates entered IP addresses using regular expressions and checks whether the IP addresses are pingable. 
  It provides the ability to continue validating and checking IPs until the user decides to exit. 
  The program also records the results of validation and ping checks in a text file named ip_list.txt.
Usage:
  1.Copy the provided Python code into a .py file on your local machine.
  2.Run the program using a Python interpreter:
    python ip_validation_and_ping_check.py
    The program will prompt you to enter an IP address for validation and ping check.
  3.If the IP address is valid based on the regular expression, the program will attempt to ping it. The results of validation and ping checks will be displayed, and they will be recorded in the ip_list.txt file.
  The program will continue to prompt for IP addresses until you choose to exit by typing "exit".
  4.When you decide to exit, the program will save the validation and ping check results in the ip_list.txt file.

**Task 4: Employee Details Generator using Random Module:**

This Python program generates employee details using the random module. The program generates random employee IDs, locations, and salaries based on specified ranges and options. Here's a breakdown of the program's functionality:

Employee Details Generated:

Employee ID (1 to 9999): Randomly generated unique identification numbers.
Employee Location: Dynamically selects a city from the given list (Kormangala, HSR Layout, Ballary, Mumbai, Chennai, Nellore, Gurgaon, Hyderabad).
Employee Salary (20,000 to 1,50,000): Randomly generated salary amounts within the specified range.
Input from Command Line:

The program takes input from the command line to determine how many employee details to generate and display.
Generators and Yield:

The employee details are generated using generator concepts, utilizing the yield statement. This allows for memory-efficient generation of details on-the-fly.
Displaying Employee Details:

The next() function is used to retrieve the next set of generated employee details, which are then displayed on the console.
This program is useful for generating realistic employee data for testing and demonstration purposes. It demonstrates the use of randomization, input handling, and generator concepts in Python programming.

**Task 5: Multiple Producers and Multiple Consumers using Threads:**

This Python program demonstrates the concept of multiple producers and multiple consumers using threads. It showcases a concurrent scenario where producers generate items and consumers consume them concurrently, making use of the threading module.
  
The program utilizes the threading module in Python to implement multi-threading.

The user is prompted to input the number of producers and consumers to simulate the functionality.
Producers create items while consumers consume them concurrently using threads.

How to Run
1.Clone the repository or download the Python script.

2.Open a terminal and navigate to the directory containing the script.

3.Run the script using the following command:
python Threading.py
Follow the prompts to enter the number of producers and consumers.

Program Components
Producers: These threads simulate producers generating items in a concurrent manner.
Consumers: These threads simulate consumers consuming items concurrently.
Thread Synchronization: The program utilizes synchronization mechanisms like locks to prevent race conditions while accessing shared resources.

Benefits
Illustrates the concept of multi-threading and concurrency in Python.
Demonstrates the usage of thread synchronization mechanisms for ensuring data consistency.

Use Cases
Demonstrating parallel processing and concurrency in scenarios involving multiple producers and consumers.

**Task 6: Area Calculation using Inheritance and Function Overloading:**

This Python program calculates the area of various shapes, including squares, triangles, and circles, by leveraging the concepts of inheritance and function overloading. The Shape class serves as the base class, and specific shapes inherit from it to calculate their respective areas.

Program Overview
The program employs the principles of object-oriented programming, inheritance, and function overloading to calculate shape areas.
It showcases the versatility of Python's object-oriented features.

How to Run
Clone the repository or download the Python script.

Open a terminal and navigate to the directory containing the script.

Run the script using the following command:
python Shape.py
Follow the prompts to provide necessary dimensions for calculating shape areas.

Program Components
Shape Class: The base class Shape defines the area() method as a placeholder to be overridden by derived shape classes.

Derived Shape Classes: The Square, Triangle, and Circle classes inherit from Shape and provide their own implementations of the area() method.

Function Overloading: By overriding the area() method, the derived classes achieve function overloading, allowing each shape to calculate its area using specific formulas.

Benefits
Demonstrates the principles of inheritance and function overloading in Python.
Illustrates how object-oriented programming enables code reusability and extensibility.

Use Cases
Implementing area calculations for various shapes in applications like graphics software or geometry calculators.
Enhancing programming skills in object-oriented design and implementation.