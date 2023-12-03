import os

# Get a list of all files in the directory
all_files = os.listdir(os.path.dirname(__file__))

# Filter out files that are not Python files or the __init__.py itself
py_files = [file[:-3]
            for file in all_files if file.endswith('.py') and file != '__init__.py']

# Import all modules in this directory
for module_name in py_files:
    __import__(module_name, globals(), locals(), level=1)
