[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/)
# Read books tracker
Essential interface-model-database system to store the information about the books one reads.

## Goal of the project
Imagine that you read a lot of books. Imagine also that you have no idea about how databases and graphical user interfaces (GUIs) work but you would like to learn.

Well, I don't know about you, but I found myself in the situation above and I thought that the most logical thing to do would be just one: coding a simple system to store the information about the books I read. In a MySQL database. With a GUI.

# Usage
## How to run the code
To run this code, you should first download the files in the directory. You can do it manually or by cloning the repo:
```console
git clone https://github.com/FilippoPisello/Books-Read-DB
```
Only for the first use, the schema and tables should be created with this command:
```console
python -m database.db_creation
```
To run the actual tool, you should go in the directory and run the following command:
```console
python -m book_db_logger
```
The GUI will pop up.

## Requirements & Dependencies
To correctly execute the code there are some DB requirements to be fulfilled and some external libraries to be installed.
### DB Requirement
For the code to run:
- MySQL should be installed on the device
- MySQL service should be running
### Required Libraries
The following external libraries are required:
- gooey
- mysql
