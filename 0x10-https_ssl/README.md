# HTTPS SSL
* The 2 main elements that SSL (Secure Sockets Layer) provides:
  SSL (Secure Sockets Layer) is a protocol that provides encryption and authentication for data transmission over the internet.
* SSL primarily offers two main elements:
> * Encryption: SSL uses cryptographic techniques to encrypt data during transmission.
> * This means that the data is transformed into a secure format that can only be deciphered by the intended recipient.
> * Authentication: SSL provides authentication by verifying the identity of the server (and optionally, the client) in a communication.
> *  This authentication is done through digital certificates, which are issued by trusted Certificate Authorities (CAs). When a client connects to a server using SSL, it can verify that it's communicating with the legitimate server and not an impostor.
* HAProxy SSL termination on Ubuntu 16.04:
> * HAProxy is a popular open-source load balancer and proxy server that can be used to distribute incoming traffic to multiple backend serve
> * SSL termination is a process where the SSL encryption and decryption are handled at the load balancer or proxy server (in this case, HAProxy) rather than at the backend web servers. Here's a brief explanation:
> * SSL Termination: In an SSL termination setup, HAProxy is responsible for handling the SSL/TLS encryption and decryption. When a client (e.g., a web browser) makes an HTTPS request to HAProxy, it decrypts the request, inspects it, and then forwards the unencrypted request to one of the backend web servers.
> * When the backend web server sends its response back to HAProxy, HAProxy re-encrypts it before sending it to the client. This offloads the SSL processing from the backend servers and can improve performance and security.
> * Ubuntu 16.04: This refers to the specific version of the Ubuntu operating system (which reached its end-of-life in April 2021). When configuring HAProxy for SSL termination on Ubuntu 16.04, you would follow the relevant setup procedures for your HAProxy version and configure SSL certificates, frontend and backend configurations, and any necessary security settings on this Ubuntu server.
* Bash Function:
> * A Bash function is a reusable block of code within a Bash script or shell session. It allows you to group commands and statements together, giving them a name and optional parameters.
> *  Functions are used to make your shell scripts more organized, modular, and easier to maintain. They can be called multiple times within a script, making it easier to perform specific tasks or calculations.
