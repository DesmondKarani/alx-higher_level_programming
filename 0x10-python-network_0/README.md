# 0x10. Python - Network #0

This project is about learning the basics of HTTP and how to use Python scripts to interact with web servers.

## Description

In this project, we will learn:

- What a URL is
- What HTTP is
- How to read a URL
- The scheme for a HTTP URL
- What a domain name is
- What a sub-domain is
- How to define a port number in a URL
- What a query string is
- What an HTTP request is
- What an HTTP response is
- What HTTP headers are
- What the HTTP message body is
- What an HTTP request method is
- What an HTTP response status code is
- What an HTTP Cookie is
- How to make a request with cURL
- What happens when you type google.com in your browser (Application level)

## Requirements

- A README.md file, at the root of the folder of the project, is mandatory
- All scripts will be tested on Ubuntu 20.04 LTS
- All Bash scripts should be exactly 3 lines long (wc -l file should print 3)
- All files should end with a new line
- All files must be executable
- The first line of all bash files should be exactly #!/bin/bash
- The second line of all Bash scripts should be a comment explaining what is the script doing
- All curl commands must have the option -s (silent mode)
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- The first line of all Python files should be exactly #!/usr/bin/python3
- Your code should use the pycodestyle (version 2.8.*)
- All modules should be documented: python3 -c 'print(__import__("my_module").__doc__)'
- All classes should be documented: python3 -c 'print(__import__("my_module").MyClass.__doc__)'
- All functions (inside and outside a class) should be documented: python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Resources

Read or watch:

- HTTP (HyperText Transfer Protocol) (except: “TRACE” Request Method, “CONNECT” Request Method, Language Negotiation and “Options MultiView” and Character Set Negotiation)
- HTTP Cookies

## Tasks

0. cURL body size
Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

1. cURL to the end
Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response

2. cURL Method
Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response

3. cURL only methods
Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.

4. cURL headers
Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response

5. cURL POST parameters
Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response

6. Find a peak
Write a function that finds a peak in a list of unsorted integers.

7. Only status code
Write a Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.

8. cURL a JSON file
Write a Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.

9. Catch me if you can!
Write a Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response.
