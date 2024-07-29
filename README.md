MyAmazon
MyAmazon is a simple console-based application for user registration, login, and product management. The application demonstrates basic concepts of Object-Oriented Programming (OOP), file handling, and user interaction.

Features
User Registration and Login: Allows new users to register and existing users to log in.
Product Management: Displays available products and handles purchases.
CSV File Storage: Stores user and product information in CSV files.

Structure
The code is organized into the following files:

amazon.py: Main script to handle user interactions and product selection.
auth_for_myamazon.py: Contains the register class for user registration and login.
products_for_myamazon.py: Contains the avalprod class for managing and purchasing products.


Key Concepts
1. Class and Object-Oriented Programming (OOP)
Classes and Objects:
register: Manages user registration and login.
avalprod: Manages product-related actions like displaying available products and handling purchases.
2. File Handling
CSV Files:
custdata.csv: Stores user data.
store.csv: Stores product data.
Writing to CSV: Data is written using csv.writer.
Reading from CSV: User data is read using csv.reader.
3. User Input and Output
Input: Uses input() to gather user details, login credentials, and product selections.
Output: Uses print() to display messages, prompts, and results.
4. Control Flow
Conditional Statements: Controls the flow based on user choices with if, elif, and else statements.
5. Recursive Function Calls
Recursion: Methods in avalprod (electronics(), fashion(), stationary()) call themselves if an invalid choice is made, allowing users to try again.
6. Error Handling
Basic Error Handling: The code does not include explicit error handling for issues like file not found or input errors. Consider adding try-except blocks for improved robustness.
7. Data Encapsulation
Attributes and Methods: Classes encapsulate data (e.g., uname, phno, address) and behaviors (e.g., reg(), login(), electronics()).
8. Instance Methods and Attributes
Instance Methods: Operate on instance data, managing user and product interactions.
Instance Attributes: Store data specific to class instances.
9. Code Organization
Modularization: Code is divided into separate files for better organization and functionality separation.
