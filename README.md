# Python-Mini-Project

<h3>Title: Expense Tracker System</h3>
Submitted by: Aabha Amol Dahale<br>
Submitted to: Dr. R. S. Khamitkar<br>
Department: Electronics and Computer Engineering<br>
Date: 10/04/2026<br>

1. Project Overview<br>

This project is a Python-based Expense Tracker System developed using the Tkinter GUI library. The application allows users to input daily expenses, store them in a file, and perform operations such as viewing all expenses and calculating the total expenditure. The system ensures persistent data storage using file handling and provides an interactive graphical interface for better usability.

2. Problem Statement<br>

Manual tracking of daily expenses is inefficient and prone to errors. Users require a simple and effective system to:<br>
 Record expenses<br>
 View stored data<br>
 Calculate total spending<br>
This project aims to develop a GUI-based Python application that efficiently manages expense data and simplifies financial tracking.

3. Technology Stack<br>
 Programming Language: Python 3.x<br>
 GUI Library: Tkinter<br>
 IDE: Python IDLE<br>
 Storage: Text File (expenses.txt)<br>

4. Implementation<br>
The implementation is based on the following structured logic:<br>
Input Handling<br>
 User enters:<br>
 Expense name<br>
 Expense amount<br>

Validation<br>
 Ensures fields are not empty<br>
 Converts amount into float<br>
 Displays error for invalid input<br>

Data Storage<br>
Data is appended to a text file in format:<br>
Name,Amount

Viewing Data<br>
 Reads file line by line<br>
 Displays data in Listbox<br>
Total Calculation<br>
 Extracts amounts from file<br>
 Calculates total using loop<br>

GUI Components<br>
 Labels and Entry fields<br>
 Buttons for different operations<br>
 Listbox for display<br>

5. Results and Observations<br>
 The system successfully stores expense data in a file<br>
 GUI makes the system interactive and user-friendly<br>
 Total expense calculation works accurately<br>
 Supports multiple entries without data loss<br>
