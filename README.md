# Python-Mini-Project
Expense Tracking System

Title: Expense Tracker System

Submitted by: Aabha Amol Dahale

Student Roll No: 10

Student Enrollment ID: 2403111019

Submitted to: Dr. R. S. Khamitkar

Department: Electronics and Computer Engineering

Date: 10/04/2026

1. Project Overview

This project is a Python-based Expense Tracker System developed using the Tkinter GUI
library. The application allows users to input daily expenses, store them in a file, and perform
operations such as viewing all expenses and calculating the total expenditure.
The system ensures persistent data storage using file handling and provides an interactive
graphical interface for better usability.

2. Problem Statement

Manual tracking of daily expenses is inefficient and prone to errors. Users require a simple and
effective system to:
 Record expenses
 View stored data
 Calculate total spending
This project aims to develop a GUI-based Python application that efficiently manages expense
data and simplifies financial tracking.

3. Technology Stack

 Programming Language: Python 3.x
 GUI Library: Tkinter
 IDE: Python IDLE
 Storage: Text File (expenses.txt)

4. Implementation

The implementation is based on the following structured logic:
Input Handling
 User enters:
 Expense name
 Expense amount
Validation
 Ensures fields are not empty
 Converts amount into float
 Displays error for invalid input
Data Storage
Data is appended to a text file in format:
Name,Amount
Viewing Data
 Reads file line by line
 Displays data in Listbox
Total Calculation
 Extracts amounts from file
 Calculates total using loop
GUI Components
 Labels and Entry fields
 Buttons for different operations
 Listbox for display

5. Results and Observations

 The system successfully stores expense data in a file
 GUI makes the system interactive and user-friendly
 Total expense calculation works accurately
 Supports multiple entries without data loss