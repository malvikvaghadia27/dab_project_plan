from setuptools import setup, find_packages

setup(
    name="dab_project_plan",
    version="0.0.1",
    description="project_description",
    author="Malvik Vaghadia",
    packages=find_packages(where="./src"),
    package_dir={"": "./src"},
    install_requires=[
        "setuptools"]
)