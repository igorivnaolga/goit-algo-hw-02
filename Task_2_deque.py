# Необхідно розробити функцію, яка приймає рядок як вхідний параметр, додає всі його символи 
# до двосторонньої черги (deque з модуля collections в Python), 
# а потім порівнює символи з обох кінців черги, щоб визначити, чи є рядок паліндромом. 
# Програма повинна правильно враховувати як рядки з парною, так і з непарною кількістю символів, 
# а також бути нечутливою до регістру та пробілів.

from collections import deque

def check_palindrom(input_string):
    cleaned = ''.join(c.lower() for c in input_string if c.isalnum())
    
    cleaned_string = deque(cleaned)

    while len(cleaned_string) > 1:
        if cleaned_string.popleft() != cleaned_string.pop():
            return False
        
    return True


print(check_palindrom("Was it a car or a cat I saw?"))     
print(check_palindrom("A man a plan a canal Panama"))
print(check_palindrom("Hello"))  
print(check_palindrom("123454321"))
print(check_palindrom("No l em  on, no mel  on"))               # True
