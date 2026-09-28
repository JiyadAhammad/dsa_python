## Understanding HTTP for backend engineers, where it all starts

# HTTP Protocol
    The medium where our browser talks to our servers either to send data or to receive data from it
    Two ideas which are heart of HTTP:
    1. Stateless
        It has no memory of past interactions. Each HTTP request carries all the necessary information for the server to process it (headers, urls, methods), After the server response it forget about the requests. If client sent new request it treat as new request or events
        Each request need specific information to process the data like Authentication information such as tokens, session etc
        **Benefits :**
            Simplicity
            Scalability
        To maintain the continuity of interaction client uses state management to store cookies

    2. Client-server Model

    Main two protocols used for http requests are:
    1. TCP -> Transfer control protocol
    2. UDP -> User Datagram Protocol

    OSI Reference model => When sending and receiving data
        From top to bottom, the layers are:
        Layer 7 - Application Layer: Acts as the direct interface between the user's software application and the network Examples: HTTP, DNS, FTP.
        Layer 6 - Presentation Layer: Formats, encrypts, and compresses data so the receiving application can read it.
        Layer 5 - Session Layer: Manages and controls the dialogue and connections between devices.
        Layer 4 - Transport Layer: Ensures reliable, end-to-end delivery of entire messages and breaks data into segments. Examples: TCP, UDP.
        Layer 3 - Network Layer: Handles logical addressing (IP addresses) and routes data packets across different networks.Layer 2 - Data Link Layer: Frames packets and handles physical node-to-node or MAC addressing.
        Layer 1 - Physical Layer: Transmits raw, unstructured bitstreams of data across physical hardware media like cables or radio signals.

    Evolution of http. => HTTP/0.9, HTTP/1.0, HTTP/1.1, HTTP/2, HTTP/3,

    **Messages:**
        1. Request
            POST /api/user/1234 HTTP/1.1 ==> Method, End point, http version
            HOST: example.com ==> Frontend domain
            Headers: user-agent, content-type, content-length, Authorization, accept, accept-encoding, connection, cookies etc 

            // a blank line here means, all headers are over, everything has been sent

            Request body: -> Information client want to send
                {
                    "username": "john",
                    "email": "john@example.com",
                    "age": 28,
                    "is_active": true
                }
            
        2. Response
            HTTP/1.1 200 ok ==> http version, status code, value of status code
            Headers: Date, content-type, content-length, server, cache-control, X-request-ID:, etc...

            // a blank line here means, all headers are over, everything has been sent

            Response body: -> Information send back to client
            {
                "message": "User Update Successfully",
                "status": "Success",
                "data": {
                    "id": 1042,
                    "username": "john",
                    "email": "john@example.com",
                    "is_active": true,
                    "roles": [
                    "user",
                    "administrator"
                    ],
                    "profile": {
                    "first_name": "John",
                    "last_name": "Doe",
                    "avatar_url": null
                    }
                }
            }
        ```
            ## Headers -> Headers are basically Key value pairs
            Why headers? -> To know about the sent and receiver easily 
            **Request headers:** 
                1. user-agent -> Identifies what type of client is that (browser, postman, mobile app)
                2. Authorization -> Send different types of credentials (Bearer tokens)
                3. Cookies ->
                3. Accept -> What kind of content we accept (json, text, html)
            **General headers:**
                1. Date -> Date of request or response
                2. cache-control -> Caching mechanism used (no-cache)
                3. connection -> Connection information (keep-alive)
            **Representation Headers:**
                1. Content-type  -> Media type
                2. content-length -> size of the request
                3. content-encoding -> encoding tricks (Gzip)
                4. etag -> A unique identifier which is mostly use for caching
            **Security Headers:**
                1. strict-transport-security(HSTS) -> Client only communicate the server with https
                2. content-security-policy -> Restrict the content loads
                3. x-frame-options -> prevent the websites to 
                4. x-content-type-options
                5. set-cookies
        ```

    1. Extensibility
        Https headers can be easily added or customize without altering the underline protocol
    2. Remote control
        Http headers act as remote control on server side, they allow to the client to send instructions to the server influence how the server responding or process the request (Content type negotiation)

    **HTTP Methods:** Method defined the intent of request 
        1. GET -> Fetch data from server
        2. POST -> Create data into the server. Post have a request body
        3. PUT -> Update data (Replace the entire data)
        4. PATCH -> Partial update of data (Selective replacement)
        5. DELETE -> Delete kinds of resources
        6. OPTION -> Options method is used to fetch the capability of the server for a  cross origin request Which is used in the CORS flow
    **Idempotent vs Non-idempotent**
        Idempotent: Multiple request which can cause same result (GET, PUT, DELETE)
        Non Idempotent: Request treat as a new item when multiple types happens (POST)
    