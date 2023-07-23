# First 九 tasks
* Your first challenge is to print "hello world" on the terminal in a single command.
* Print the current working directory.
* List names of all the files in the current directory, one file per line.

* Print the last 5 lines of "access.log" ==> tail -n 5 access.log

* Create an empty file named take-the-command-challenge in the current working directory.
* Create a directory named tmp/files in the current working directory ==> mkdir -p tmp/files

* Copy the file named take-the-command-challenge to the directory tmp/files

* Move the file named take-the-command-challenge to the directory tmp/files
> > * ln -s tmp/files/take-the-command-challenge take-the-command-challenge
* Delete all of the files in this challenge directory including all subdirectories and their contents. 
> * find -mindepth 1 -delete
* There are files in this challenge with different file extensions. Remove all files with the .doc extension recursively in the current working directory.
> * find . -type f -name "*.doc" -delete
* There is a file named access.log in the current working directory. Print all lines in this file that contains the string "GET".
> * grep "GET" access.log (grep -i "GET" access.log - is case insensitive)
* Print all files in the current directory, one per line (not the path, just the filename) that contain the string "500".
> * grep -l "500" * | xargs -n 1 basename
* Print the relative file paths, one path per line for all filenames that start with "access.log" in the current directory.
> * find . -type f -name "access.log*" -printf "%P\n"find . -type f -name "access.log*" -printf "%P\n"
* Print all matching lines (without the filename or the file path) in all files under the current directory that start with "access.log" that contain the string "500".
* Note that there are no files named access.log in the current directory, you will need to search recursively.
> * grep -r -h "500"
* Extract all IP addresses from files that start with "access.log" printing one IP address per line.
> * grep -ro ^[0-9.]*
* Count the number of files in the current working directory. Print the number of files as a single integer.
> * find . -type f | wc -l
* Print the contents of access.log sorted. >> sort access.log
* Print the number of lines in access.log that contain the string "GET".
> * grep GET access.log | wc -l
* The file split-me.txt contains a list of numbers separated by a ; character.
* Split the numbers on the ; character, one number per line.
> * cat split-me.txt | tr ";" "\n"
* Print the numbers 1 to 100 separated by spaces ==> echo {1..100}

* This challenge has text files (with a .txt extension) that contain the phrase "challenges are difficult". Delete this phrase from all text files recursively.
* Note that some files are in subdirectories so you will need to search for them.
> * sed -i 'challenge are difficult/d' **/*.txt
* The file sum-me.txt has a list of numbers, one per line. Print the sum of these numbers.
> * jq -s add sum-me.txt
* Print all files in the current directory recursively without the leading directory path.
* Rename all files removing the extension from them in the current directory recursively.
> * mv * .*
* The files in this challenge contain spaces. List all of the files (filenames only) in the current directory but replace all spaces with a '.' character.
> * ls | tr ' ' '.'
* In this challenge there are some directories containing files with different extensions. Print all directories, one per line without duplicates that contain one or more files with a ".tf" extension.
> * dirname **/*tf | sort -u
* There are a mix of files in this directory that start with letters and numbers. Print the filenames (just the filenames) of all files that start with a number recursively in the current directory.
> * find -type f -printf '%f\n' | grep ^[0-9]

























