# goit-algo-hw-02

# Task 1

You need to develop a program that simulates the reception and processing of requests:
The program should automatically generate new requests (identified by a unique number or other data), add them to a queue, and then sequentially remove them from the queue for "processing", thus simulating the operation of a service center.

Here’s the pseudocode for the task using a queue (from the queue module in Python) for the request processing system:

queue = Queue()

Function generate_request():
Create a new request
Add the request to the queue

Function process_request():
If the queue is not empty:
Remove a request from the queue
Process the request
Else:
Display a message that the queue is empty

Main program loop:
While the user does not exit the program:
Call generate_request() to create new requests
Call process_request() to process requests
This pseudocode uses two main functions:

generate_request() generates new requests and adds them to the queue.

process_request() processes requests by removing them from the queue.
The main loop of the program executes these functions, simulating a continuous flow of new requests and their processing.

# Task 2

You need to develop a function that takes a string as an input parameter, adds all its characters to a double-ended queue (deque from the collections module in Python), and then compares characters from both ends of the queue to determine whether the string is a palindrome.

The program should properly handle strings with both even and odd numbers of characters, and it should be case-insensitive and ignore spaces.
