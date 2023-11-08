# Web stack debugging #3

# Resolving an HTTP 500 error using TMUX and STRACE
* Error 500 is an internal server error that indicates something 
  has gone wrong on the server's side.It's an application error.

* Trouble shoot the application using tmux and strace.
* Strace - is used to monitor the system calls been made by a command or a process already in progress.
           More like spying on an executable or a process.
* Tmux - is used to create multiple sessions of a shell session, so you can have multiple processes running, taking
         the shell interface and still be able to do other things at the same time.
> * service apache2 status - check that apache is installedd and running
> * ss -tuna | grep 80 -  confirm that port 80 is listening on the server.
> * curl -sI localhost - confirm the error
> * tmux new-session -s session1 - create new session using tmux.
> * ctrl +B then C - create a new window
> * lsof -i:80 - checks the PID of the apache process
> * strace -p [PID] - for monitoring the process
