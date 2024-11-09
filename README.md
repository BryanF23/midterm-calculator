IS 218 midterm-calculator

Clone the repository:
git clone: https://github.com/BryanF23/midterm-calculator.git
cd midterm-calculator
Create an (venv) virtual environment:

Using python -m venv venv to install it
source venv/bin/activate 

Installing Dependencies
The workflow first updates ‘pip’ and then installs the required libraries from ‘requirements.txt’ to set up the environment for testing.

The GitHub Actions workflow makes the setup and testing by setting up the environment, I installed the dependencies from requirements.txt, ran tests with pytest, and generated coverage reports. It is triggered by changes to the main branch and ensures it runs if 100% test coverage is possible. The code also involves tests for the Calculator and History classes, which fix and handle invalid inputs, errors, and empty histories. 

The core functionality is built around the Calculator class that supports basic operations. The History class tracks calculations and lets users undo clear, save, and load history. An abstract 'Operation' class defines the structure for operations, the calculator interacts with the user's commands from the main.py file to display the results.

REPL in main
Use the REPL: to created basic functions (add, subtract, multiply, divide)

Environment Variables
Environment variables are set up to keep sensitive or configurable settings separate from the main codebase, making it more secure and flexible. Variables such as API keys, debug levels, or paths are stored in a `.env` file and accessed via a configuration module. This setup allows the calculator to behave differently depending on the environment (e.g., development, testing, production).

Logging
The calculator uses logging to track actions, errors, and user activity, which helps with debugging and monitoring. 

 Exception Handling - LBYL and EAFP ("Look Before You Leap" and "Easier to Ask for Forgiveness than Permission")
1. Look Before You Leap: It's used when we check conditions before running code that could cause errors. For example, we check if a variable is not None before using it.
2. Easier to Ask for Forgiveness than Permission: It's used when it's more efficient to handle errors as they happen rather than checking for every possible problem in advance. For example, division operations use a try/except block to catch a 'ZeroDivisionError' instead of checking if the divisor is zero first.

GitHub Actions Workflow 
Environment variables like API keys used in the calculator app can be in the .env file, which is read when run.

python -m pip install --upgrade pip
pip install -r requirements.txt  # Install all dependencies from requirements.txt
  
Running Tests with Coverage
You run pytest to execute tests while checking the test coverage. The --cov part is what tests it when run, and the --cov-fail-under=100 flag makes sure the tests will fail if coverage is below 100%.

Generating a Coverage Report
To generate a coverage report use run the coverage report command  and it prints a summary of the coverage report to the console

Video: https://youtu.be/-1Nii5Fg8eg
