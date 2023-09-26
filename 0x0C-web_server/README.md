# Web server
* The main role of a web server is to handle incoming requests from clients (usually web browsers) and serve web content in response to those requests
* A child process is a separate, independent process that is created by a parent process.
* HTTP (Hypertext Transfer Protocol) defines several methods or HTTP requests that clients (e.g., web browsers) can use to interact with web servers. The main HTTP requests include:
> * GET: Used to request data from a specified resource. Typically used for retrieving web pages, images, and other static content.
> * POST: Used to submit data to be processed to a specified resource. It can be used for tasks like submitting forms, uploading files, or sending data to a server for processing.
> * PUT: Similar to POST, but it is often used to update or replace an existing resource at the specified URL. It should be idempotent, meaning that making the same PUT request multiple times should have the same result as making it once.
> * DELETE: Used to request the removal of a specified resource. It instructs the server to delete the resource at the given URL.
> * PATCH: Used to apply partial modifications to a resource. It is often used when you want to update a resource's attributes without affecting the entire resource.
> * HEAD: Similar to GET, but it requests only the headers of a resource without the actual content. It is often used for checking resource metadata or determining if a resource has been modified.
> * OPTIONS: Used to request information about the communication options available for a resource. It is often used to check which HTTP methods are supported for a particular URL.
* A (Address) Record:
> * The A record maps a domain name to an IPv4 address. 
* AAAA (IPv6 Address) Record:
> * The AAAA record, also known as a quad-A record, maps a domain name to an IPv6 address.
* CNAME (Canonical Name) Record:
> * The CNAME record is used to create an alias or nickname for an existing domain.
* MX (Mail Exchanger) Record:
> * The MX record specifies the mail servers responsible for receiving email messages on behalf of a domain.
* TXT (Text) Record:
> * The TXT record allows domain owners to attach human-readable text to a domain name.
* NS (Name Server) Record:
> * The NS record specifies the authoritative name servers for a domain. 
* SOA (Start of Authority) Record:
> * The SOA record contains administrative information about a domain, such as the primary name server, contact email address, and details about the domain's refresh, retry, expire, and TTL (Time to Live) settings. 
* PTR (Pointer) Record:
> * The PTR record is used for reverse DNS (rDNS) lookup.
* SRV (Service) Record:
> * The SRV record specifies the location of services within a domain.
* CAA (Certificate Authority Authorization) Record:
> * The CAA record allows domain owners to specify which certificate authorities are authorized to issue SSL/TLS certificates for their domain. 
