import queue
import time
import random

request_queue = queue.Queue()

request_id = 0

def generate_request():
    global request_id
    request_id += 1
    request = f"Request #{request_id}"
    request_queue.put(request)
    print(f"Added: {request}")


def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"In process: {request}")
        time.sleep(random.uniform(0.5, 1.5))
        print(f"Completed: {request}")
    else:
        print("Empty queue.")


def main():
    try:
        while True:
            action = input("\nEnter 'g' to generate request, 'p' to process request, 'e' to exit: ").strip().lower()

            if action == 'g':
                generate_request()
            elif action == 'p':
                process_request()
            elif action == 'e':
                print("Exit")
                break
            else:
                print("Unknown command")

    except KeyboardInterrupt:
        print("\nProgram was interrupted")


if __name__ == "__main__":
    main()

