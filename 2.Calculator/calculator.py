def add(a, b):
    answer = a + b
    print(f'Result from a + b = {answer}')
def subs(a, b):
    answer = a - b
    print(f'Result from a - b = {answer}')
def mul(a, b):
    answer = a * b 
    print(f'Result from a * b = {answer}')
def div(a, b):
    answer = a / b
    print(f'Result from a / b = {answer}')



while True:
    print("A. Addition")
    print("B. Substraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")
    choice2 = input("input your choice: ")
    choice = choice2.lower()
    
    if choice not in ('e', 'a', 'b', 'c', 'd'):
        print('your input is not valid')
    elif choice == 'e':
        print("Thank you. Have a nice day!")
        quit()
    elif choice == 'a':
        print(f'Addition')
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        add(a, b)
    elif choice == 'b':
        print(f'Substraction')
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        subs(a, b)
    elif choice == 'c':
        print(f'Multiplication')
        a = int(input("Input second number: "))
        b = int(input("Input second number: "))
        mul(a, b)
    elif choice == 'd':
        print(f'Division')
        a = int(input("Input second number: "))
        b = int(input("Input second number: "))
        div(a, b)
