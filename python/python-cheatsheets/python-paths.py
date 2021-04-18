import os
import sys

# The __file__ variable path of the current module file (defined only when executing the Python script externally)
print(__file__)

# Get the current working directory
print(os.getcwd())

# Set the current working directory
os.chdir("/tmp/")

# Insert a new entry into the path, at a specified position. In this example, inserts the parent of the working dir
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# Read contents of directory
info_files_in_dir = [f for f in os.scandir("/tmp/")]

for finfo in info_files_in_dir:
    print(f"File: {finfo.name}. Last modified: {finfo.stat().st_mtime}")

