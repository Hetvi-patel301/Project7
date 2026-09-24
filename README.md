# Multi-Utility Toolkit

### Introduction

The **Multi-Utility Toolkit** is a simple Python menu-driven program that provides multiple utilities using Python's built-in modules and custom modules.

The program contains different operations such as date and time handling, mathematical calculations, random data generation, UUID generation, file handling, and exploring module attributes.

The program continues running until the user selects the **Exit** option.

### Main Functionalities

1. Date and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations
6. Explore Module Attributes using `dir()`
7. Exit

### Features

- Display the current date and time.
- Calculate the difference between two dates and times.
- Format dates into a custom format.
- Use a stopwatch.
- Use a countdown timer.
- Calculate factorial.
- Calculate compound interest.
- Perform trigonometric calculations.
- Calculate the area of geometric shapes.
- Generate random numbers.
- Generate random lists.
- Create random passwords.
- Generate random OTPs.
- Generate UUIDs using different UUID versions.
- Create new files.
- Write data to files.
- Read data from files.
- Append data to files.
- Explore module attributes using `dir()`.
- Uses separate custom modules for different operations.
- Uses functions for reusable operations.
- Uses a menu-driven interface.
- Allows multiple operations in a single execution.
- Uses `try-except` for handling file-related errors.
- Uses `__name__` and `__main__` to control program execution.

### Core Concepts

#### Concepts Used

- Modules and Modular Programming
- Custom Modules
- Functions
- `while` loop
- `match-case`
- `if-else`
- `input()`
- `datetime` module
- `time` module
- `math` module
- `random` module
- `uuid` module
- File Handling
- Exception Handling
- `try-except`
- `with open()`
- `dir()`
- `__name__`
- `__main__`

### Script Organization

The main program is organized using a `main()` function.

The following code is used to make sure that the main menu runs only when the file is executed directly:
`python
if __name__ == "__main__":
    main()

    
###  Project Structure
Project_7/
│
├── Toolkit.py
├── module
  ├── date_time_module.py
  ├── Math_module.py
  ├── random_module.py
  ├── uuid_module.py
  ├── file_module.py
  ├── dir_module.py
  ├── __init__.py
  ├── output.md
└── README.md

**Created by:** Hetvi Patel
