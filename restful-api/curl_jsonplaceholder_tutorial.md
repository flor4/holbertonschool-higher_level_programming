
# 📘 Exercise Overview: Using `curl` to Interact with APIs

This exercise is designed to introduce you to the basic usage of `curl`, a powerful command-line tool used for transferring data over various protocols such as HTTP and HTTPS.

You'll use `curl` to perform different types of requests to a public fake API — [JSONPlaceholder](https://jsonplaceholder.typicode.com/) — which simulates real RESTful endpoints for learning and testing.

## 💡 What You'll Learn

By completing this exercise, you will understand and practice the following core concepts:

### ✅ 1. Installing and Verifying curl
- Learn how to install curl on your system.
- Use `curl --version` to verify that it's correctly installed and check the supported protocols.

### ✅ 2. Basic HTTP GET Requests
- Fetch content from a regular webpage using `curl`.
- Understand how a browser-like tool can retrieve web data from a server.

### ✅ 3. Interacting with a REST API (GET, POST)
- Use `curl` to make `GET` requests to retrieve data from an API.
- Make `POST` requests to simulate sending data to the server.
- Learn how to pass data using the `-d` (data) option.

### ✅ 4. Reading HTTP Response Headers
- Learn how to inspect only the response headers using the `-I` option.
- Understand useful header fields like `Content-Type`, `Cache-Control`, `Status`, etc.

### ✅ 5. Working with JSON Data (Optional)
- Practice viewing raw JSON responses.
- Optionally, use tools like `jq` to pretty-print and navigate JSON outputs.

## 🌐 Real-World Use Cases

These are essential skills for:
- Testing and debugging REST APIs.
- Rapid prototyping of API calls without writing code.
- Inspecting server behavior and HTTP responses.

---

This exercise gives you hands-on experience with HTTP requests and shows how APIs work under the hood — using nothing but the command line.

## Instructions for Using curl 🚀

### 1. Installing and Basic Interaction with curl 🛠️

- Install **curl** on your system.  
  It's usually available in standard repositories for Linux/Mac systems.  
  For Windows, consider using Windows Subsystem for Linux (WSL) or download a Windows version of curl.  
- Once installed, confirm its availability by running:  
  ```bash
  curl --version


* Use curl to fetch the content of a webpage. For example:

  ```bash
  curl http://example.com
  ```


## 2. Fetching Data from an API 📡

* Use curl to retrieve posts from JSONPlaceholder:

  ```bash
  curl https://jsonplaceholder.typicode.com/posts
  ```
* Observe the output. It should be a JSON array of posts.

---

## 3. Using Headers and Other Options with curl ⚙️

* Fetch **only the headers** of the same request using:

  ```bash
  curl -I https://jsonplaceholder.typicode.com/posts
  ```
* Use curl to make a **POST** request to the same API:

  ```bash
  curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
  ```

---

> 💡 **Tips:**
>
> * The `-I` flag fetches only response headers (useful for checking status, content type, etc.).
> * The `-X` flag specifies the HTTP method (GET, POST, PUT, DELETE...).
> * The `-d` flag sends data in the request body (typically with POST, PUT, PATCH).
> * Use tools like [`jq`](https://stedolan.github.io/jq/) to pretty-print JSON output.



## 🌐 Simulates Real RESTful Endpoints for Learning and Testing 🧪📡

The JSONPlaceholder API provides fake but realistic RESTful endpoints for hands-on practice.  
It allows you to safely test `GET`, `POST`, and other HTTP methods without affecting any real data.  
Perfect for learning how APIs work under the hood! 🛠️🚀


### 1. Check curl Version

Check if curl is installed and see its version.

```bash
curl --version
```

**Output:**
```
curl 8.5.0 (x86_64-pc-linux-gnu) libcurl/8.5.0 OpenSSL/3.0.13 zlib/1.3 brotli/1.1.0 zstd/1.5.5 libidn2/2.3.7 libpsl/0.21.2 (+libidn2/2.3.7) libssh/0.10.6/openssl/zlib nghttp2/1.59.0 librtmp/2.3 OpenLDAP/2.6.7
Release-Date: 2023-12-06, security patched: 8.5.0-2ubuntu10.6
```
--- 
### 2. Fetch a Simple Webpage

Retrieve the content of example.com.

```bash
curl http://example.com
```

**Output:**

```
<!doctype html>
<html>
<head>
    <title>Example Domain</title>

    <meta charset="utf-8" />
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style type="text/css">
    body {
        background-color: #f0f0f2;
        margin: 0;
        padding: 0;
        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
        
    }
    div {
        width: 600px;
        margin: 5em auto;
        padding: 2em;
        background-color: #fdfdff;
        border-radius: 0.5em;
        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
    }
    a:link, a:visited {
        color: #38488f;
        text-decoration: none;
    }
    @media (max-width: 700px) {
        div {
            margin: 0 auto;
            width: auto;
        }
    }
    </style>    
</head>

<body>
<div>
    <h1>Example Domain</h1>
    <p>This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.</p>
    <p><a href="https://www.iana.org/domains/example">More information...</a></p>
</div>
</body>
</html>

```
---

### 3. Retrieve Posts (GET Request)

Get a list of posts from JSONPlaceholder API.

```bash
curl https://jsonplaceholder.typicode.com/posts
```

**Output:**
  ```
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
  },
  {
    "userId": 1,
    "id": 2,
    "title": "qui est esse",
    "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
  },
  {
    "userId": 1,
    "id": 3,
    "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
    "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"
  },
 [...]
  {
    "userId": 10,
    "id": 100,
    "title": "at nam consequatur ea labore ea harum",
    "body": "cupiditate quo est a modi nesciunt soluta\nipsa voluptas error itaque dicta in\nautem qui minus magnam et distinctio eum\naccusamus ratione error aut"
  }
  ```
---

### 4. Fetch Only Response Headers

Retrieve only the headers of the response.

```bash
curl -I https://jsonplaceholder.typicode.com/posts
```

**Output:**

```
HTTP/2 200 
date: Mon, 06 Oct 2025 13:06:44 GMT
content-type: application/json; charset=utf-8
access-control-allow-credentials: true
cache-control: max-age=43200
etag: W/"6b80-Ybsq/K6GwwqrYkAsFxqDXGC7DoM"
expires: -1
nel: {"report_to":"heroku-nel","response_headers":["Via"],"max_age":3600,"success_fraction":0.01,"failure_fraction":0.1}
pragma: no-cache
report-to: {"group":"heroku-nel","endpoints":[{"url":"https://nel.heroku.com/reports?s=ScCUOx%2BFXa6Rns95guRMO4Lshfg5%2FBB0tQhBvHkEp6Y%3D\u0026sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d\u0026ts=1759531806"}],"max_age":3600}
reporting-endpoints: heroku-nel="https://nel.heroku.com/reports?s=ScCUOx%2BFXa6Rns95guRMO4Lshfg5%2FBB0tQhBvHkEp6Y%3D&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&ts=1759531806"
server: cloudflare
vary: Origin, Accept-Encoding
via: 2.0 heroku-router
x-content-type-options: nosniff
x-powered-by: Express
x-ratelimit-limit: 1000
x-ratelimit-remaining: 999
x-ratelimit-reset: 1759531812
age: 27090
cf-cache-status: HIT
cf-ray: 98a560b40a15697d-CDG
alt-svc: h3=":443"; ma=86400
```
---

### 5. Send a POST Request

Simulate creating a new post by sending data.

```bash
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```

**Output:**

```
{
  "title": "foo",
  "body": "bar",
  "userId": "1",
  "id": 101
}
```
---

> **Note:**
>
> * Use `-I` to fetch headers only.
> * Use `-X` to specify HTTP method.
> * Use `-d` to send data with POST requests.

```
---

## 📑 Exercise Summary

This exercise focused on using the `curl` command-line tool to interact with HTTP-based APIs.  
The tasks covered how to perform basic operations such as retrieving web content, sending HTTP requests (GET, POST), and inspecting response headers.

The API used was [JSONPlaceholder](https://jsonplaceholder.typicode.com/), a free tool that simulates RESTful endpoints. It allows safe testing without modifying any real data.

The objective was to become familiar with how HTTP requests work, how to structure them with `curl`, and how to read and understand the responses returned by an API.

The commands used reflected common scenarios in API testing and are applicable in development, debugging, and automation contexts. ⚙️

---

## 📘 Glossary of Key Terms

| Term                                        | Definition                                                                                                                                        |
|---------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| **curl**                                    | A command-line tool used to transfer data to or from a server using various protocols (HTTP, HTTPS, FTP, etc.). Useful for interacting with APIs. |
| **API** (Application Programming Interface) | A system that allows software to communicate with other software or services via defined rules (endpoints, methods, etc.).                        |
| **HTTP Methods**                            | Actions performed in web communication. The most common are `GET` (retrieve data) and `POST` (send data).                                         |
| **GET**                                     | An HTTP method used to request data from a server. The server returns the requested resource.                                                     |
| **POST**                                    | An HTTP method used to send data to a server, often to create or update a resource.                                                               |
| **Endpoint**                                | A specific URL that an API exposes to allow interaction with a particular piece of data or functionality.                                         |
| **Headers**                                 | Metadata sent with HTTP requests and responses. Includes info like content type, status code, and cache instructions.                             |
| **Status Code**                             | A numeric code in the HTTP response that indicates the result of the request (e.g. 200 OK, 404 Not Found).                                        |
| **JSON** (JavaScript Object Notation)       | A lightweight data-interchange format commonly used in APIs for sending structured data.                                                          |
| **jq**                                      | A command-line tool for parsing and formatting JSON data. Useful for making API responses more readable.                                          |

---
