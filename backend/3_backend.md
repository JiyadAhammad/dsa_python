## What is a Backend, how do they work and why do we need them?
```
A computer that listen rest,grpc or any other through ports
    1. 80 -> HTTP
    2. 443 -> HTTPS
```

# Start from Client to server
1. Domain name ==> https://example.com/user
    * DNS **Domain Name System**
    * DNS have different type of records
        1. A Record ==> To point a particular IP
        2. CNAME Record ==> To point a particular domain or subdomain
    * Reverse proxy ==> Basically its a server -> It sits in-front of other server, so that we can manage different types of routes and configs from a centralized place instead of changing the config every single server 
        eg: Nginx
    * Request from browser -> DNS browser -> AWS Server -> Firewall -> AWS Instance -> Nginx -> Localhost:3001 (Server)

# why do we need Backends
* Server has a Centralized control of all information in between 2 client devices
* Data -> Receive, Fetch, Persist

# Why can't everything stores in frontend (it is also a device or computer)
1. Security
2. CORS 
3. Databases
4. Computing power