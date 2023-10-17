# MySQL
* A database is information that is set up for easy access, management and updating. Computer databases typically store aggregations of data records or files that contain information, such as sales transactions, customer data, financials and product information.

# SQl Replication
* If your important data is stored in an SQL database (MySQL, MariaDB, PostgreSQL, etc.), you can take advantage of some built-in replication features. These can be used to provide a failover system in case the main server goes down.
* The most basic kind of SQL replication is a Master-Slave configuration. In this scenario, you have a main database server, which is referred to as the “master” server. This server is responsible for performing all writes and updates. The data from this server is copied continuously to a “slave” server. This server can be be read from, but not written to.
* A second form of replication is called Master-Master replication. This configuration allows both servers to have “master” abilities. This means that each server can accept writes and updates and will transfer the changes to the opposite server. This configuration inherits the advantages of the master-slave setup, but also benefits from increased write performance if the writes are properly distributed by a load balancing mechanism.
* The replica database contains the same data as the master database and is used to provide redundancy and improve performance. There are different types of database replicas, including read replicas, hot standbys, and asynchronous replicas, each serving specific purposes.
* The primary purposes of a database replica are:
> * High Availability: Replicas provide redundancy and fault tolerance. In case the master database fails, a replica can take over, ensuring minimal downtime and uninterrupted access to data.
> * Load Balancing: Read replicas can be used to offload read-heavy queries from the master database, improving overall system performance and responsiveness.
> * Data Locality: Replicas can be strategically placed in different geographic locations to reduce latency for users in various regions.
> * Disaster Recovery: In the event of a catastrophic failure, database replicas can be used to restore data and maintain business continuity.
