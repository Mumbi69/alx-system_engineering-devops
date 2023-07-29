# What is my PID
* Write a Bash script that displays its own PID.

#  List your processes
* Write a Bash script that displays a list of currently running processes.
* Requirements:
> * Must show all processes, for all users, including those which might not have a TTY
> * Display in a user-oriented format
> * Show process hierarchy

# Show your Bash PID
* Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.
* Requirements:
> * You cannot use pgrep
> * The third line of your script must be # shellcheck disable=SC2009


# Show your Bash PID made easy
* Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.
* Requirements:
> * You cannot use ps

# To infinity and beyond
* Write a Bash script that displays To infinity and beyond indefinitely.
* Requirements:
> * In between each iteration of the loop, add a sleep 2

# Don't stop me now!
* We stopped our 4-to_infinity_and_beyond process using ctrl+c in the previous task, there is actually another way to do this.
* Write a Bash script that stops 4-to_infinity_and_beyond process.
* Requirements:
> * You must use kill

# Stop me if you can
* Write a Bash script that stops 4-to_infinity_and_beyond process.
* Requirements:
> * You cannot use kill or killall

# Highlander
* Write a Bash script that displays:
> * To infinity and beyond indefinitely
> * With a sleep 2 in between each iteration
> * I am invincible!!! when receiving a SIGTERM signal

# Beheaded process
* Write a Bash script that kills the process 7-highlander.

# Process and PID file
* Write a Bash script that:
> * Creates the file /var/run/myscript.pid containing its PID
> * Displays To infinity and beyond indefinitely
> * Displays I hate the kill command when receiving a SIGTERM signal
> * Displays Y U no love me?! when receiving a SIGINT signal
> * Deletes the file /var/run/myscript.pid and terminates itself when receiving a SIGQUIT or SIGTERM signal


#  Manage my process
* Write a manage_my_process Bash script that:
> * Indefinitely writes I am alive! to the file /tmp/my_process
> * In between every I am alive! message, the program should pause for 2 seconds


# Zombie
> * For every zombie process created, it displays Zombie process created, PID: ZOMBIE_PID
> * Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
> * When your code is done creating the parent process and the zombies, use the function bellow

