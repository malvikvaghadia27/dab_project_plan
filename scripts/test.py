import sys
import os

try:
    current_dir = os.path.abspath(__file__)
    project_root = os.path.abspath(os.path.join(os.path.dirname(current_dir), ".."))

    print(f"The current dir vis abspath is: {current_dir}")
    print(project_root)
    print(f"The current root vis abspath is: {project_root}")
except:
    print("didnt work")


try:
    current_dir = os.getcwd()
    project_root = os.path.abspath(os.path.join(current_dir, ".."))

    print(f"The current dir vis getcwd is: {current_dir}")
    print(project_root)
    print(f"The current root vis getcwd and abspath is: {project_root}")
except:
    print("didnt work")