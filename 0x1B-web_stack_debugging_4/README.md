# Web stack debugging #4
* ApacheBench, also known as ab, is a command-line tool developed by the Apache Software Foundation
* It is designed for load testing and benchmarking HTTP web servers. ApacheBench allows developers and system administrators to simulate various scenarios and measure the server's response under different workloads.
* Check if ApacheBench is already installed by running the ab command in the terminal.
* I'm testing how well my web server setup featuring Nginx is doing under pressure and it turns out it’s not doing well
* I'm getting a huge amount of failed requests.
* So I will be benchmarking, using ApacheBench which is a quite popular tool in the industry as it allows me to simulate HTTP requests to a web server.
* I navigated to my error logs on nginx server using the command vi /var/log/nginx/error.log
* I realized the one error that reacted itself for all the failed requests was "/usr/share/nginx/html
* This error means is that the open files have reached the allowed limit.
* The limit that was initially in this file was 15 which was way less and that why my server could not suppprt and so I was not able to handle all the requests successfully.
* To change the limit of open files at a time, we need to acces nginx file in etc directory under the default directory so I will opend it like this vi /etc/default/nginx and changed the ULIMIT to 4096. ULIMIT="-n 4096"
* Restart nginx server using the command sudo service nginx restart.
* All done!
