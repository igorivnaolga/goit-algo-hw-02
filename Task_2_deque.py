from collections import deque

def check_palindrome(input_string):
    cleaned = ''.join(c.lower() for c in input_string if c.isalnum())
    
    cleaned_string = deque(cleaned)

    while len(cleaned_string) > 1:
        if cleaned_string.popleft() != cleaned_string.pop():
            return False
        
    return True


print(check_palindrome("Was it a car or a cat I saw?"))     
print(check_palindrome("A man a plan a canal Panama"))
print(check_palindrome("Hello"))  
print(check_palindrome("123454321"))
print(check_palindrome("No l em  on, no mel  on"))               # True
