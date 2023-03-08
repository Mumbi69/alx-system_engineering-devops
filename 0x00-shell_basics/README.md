# Where am I
* This script prints the absolute path name of the current working directory.

# What's in there
* This script displays the contents list of your current directory.

# There is no place like home
* This script changes the working directory to the user’s home directory.

#  The long format
* This script displays current directory contents in a long format.

# Hidden files
* Displays current directory contents, including hidden files (starting with .). Use the long format.

# I love numbers
* Display current directory contents.

> * Long format
> * with user and group IDs displayed numerically
> * And hidden files (starting with .)

# Welcome
*  creates a directory named my_first_directory in the /tmp/ directory.

# Betty in my first directory
* Moves the file betty from /tmp/ to /tmp/my_first_directory.

# Bye bye Betty
* Deletes the file betty

# Bye bye My first directory
* Delete the directory my_first_directory that is in the /tmp directory.

# Back to the future
* changes the working directory to the previous one.

# Lists
* lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.

# File type
* prints the type of the file named iamafile. The file iamafile will be in the /tmp directory when we will run your script.

# We are symbols, and inhabit symbols
* Create a symbolic link to /bin/ls, named __ls__. The symbolic link should be created in the current working directory.

# Copy HTML files
* copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.
Consider that all HTML files have the extension .html

# Let's move
* moves all files beginning with an uppercase letter to the directory /tmp/u.
Assume that the directory /tmp/u will exist when we will run your script.

# Clean Emacs
* deletes all files in the current working directory that end with the character ~.

# Tree 
* creates the directories welcome/, welcome/to/ and welcome/to/school in the current directory.
You are only allowed to use two spaces (and lines) in your script, not more.

# Life is a series of commas, not periods
* Write a command that lists all the files and directories of the current directory, separated by commas (,).

> * Directory names should end with a slash (/)
> * Files and directories starting with a dot (.) should be listed
> * The listing should be alpha ordered, except for the directories . and .. which should be listed at the very beginning
> * Only digits and letters are used to sort; Digits should come first
> * You can assume that all the files we will test with will have at least one letter or one digit
> * The listing should end with a new line.

#  File type: School
* Create a magic file school.mgc that can be used with the command file to detect School data files. School data files always contain the string SCHOOL at offset 0.
