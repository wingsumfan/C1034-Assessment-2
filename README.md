# C1034-Assessment-2

# Project Description
This project aims to show my knowledge of the module by implementing the knowledge into a working example creating and modifying classes/objects

# Usage
Can be ran in an IDE or on Gitbash
-Requires python or python3
-Tested on Windows 11

To use in GitBash, type in "python testing.py"
To use in an IDE, run "testing.py"

# Documentation/Overview

Two classes "job" and "jobManager" have been created in the file "job.py", the class "job" holds the information required for a worker (name, category, rate, date, hours); the class "jobManager" provides all the methods for job manipulation (adding jobs, editing jobs, etc)

The file "testing.py" tests all outlined cases from the assessment description
The tests done are as follows:

-Adding Jobs\
-Adding a job with more than 6 hours\
-Adding a job that exceeds the daily work limit (8)\
-Displaying all jobs\
-Using different search methods (by category, by rate, by name and date)\
-Removing Jobs\
-Testing total cost per a worker\
-Testing the category count per a worker\
-Testing saving and loading into the CSV file (testing.csv)\
-Testing the exceptional cases\
  -A job with negative hours\
  -A job with a negative rate\
