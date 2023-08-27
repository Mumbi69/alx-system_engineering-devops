# Web Infrastructure and Design
* User Access:
> * A user types ("www.foobar.com") in their web browser.
* Domain Name (DNS):
> * The domain name "foobar.com" is registered and configured
    with a DNS record. The "www" record for the domain points to 
    the server's IP address, which is 8.8.8.8.
> Server: A single physical server with IP address 8.8.8.8
  hosts the entire web infrastructure.
* Web Server (Nginx): Nginx is installed on the server and acts as the web server
> * It handles incoming HTTP requests from users' browsers.
> * When a request for "www.foobar.com" is received, Nginx responds with static content like HTML, CSS, and images.
    It also forwards dynamic requests to the application server.
* Application Files (My Code Base):
> * My application's source code and files are hosted on the server
> * The application server reads and processes these files to generate dynamic content.

> * MySQL, a relational database management system, is installed on the server.
> * It stores and manages your website's data, like user accounts, posts, and other information.
* Communication:
> * The server communicates with the user's computer through the HTTP protocol.
> * When a user requests a page, the server sends back the requested content (static or dynamically generated) over HTTP.

* Server: A server is a computer system that hosts and serves data, applications, and services to clients (like users' web browsers).

* Domain Name (DNS): The domain name is a human-readable label used to access resources on the internet. DNS translates domain names into IP addresses, allowing users to access websites using memorable names.

* www Record: The "www" record is a CNAME DNS record type that specifies that "www.foobar.com" is an alias for the domain "foobar.com."

* Web Server: The web server (Nginx) handles static content delivery and forwards dynamic requests to the application server.

* Application Server: The application server executes your codebase and generates dynamic content in response to user interactions.

* Database: The database (MySQL) stores and manages your website's structured data.

* Communication: The server uses the HTTP protocol to communicate with users' computers, delivering web content.

> > * ISSUES
* SPOF (Single Point of Failure): Since all components are hosted on a single server, if the server fails, the entire website goes down.

* Downtime During Maintenance: If you need to deploy new code or perform maintenance, the entire server needs to be taken down, resulting in downtime for users.

* Scalability: This infrastructure cannot handle a significant increase in traffic. If there's a sudden surge, the server might get overwhelmed and slow down or crash. 

> * Addressing these issues would involve implementing redundancy, load balancing, and scalability measures such as using multiple servers, load balancers, and cloud services.
