# is_multiple.py
    #Function takes two integer values (n, m) and returns true if n is a multiple of m

# Function definition
def is_multiple(n, m):
    # Test for errors
    try:
        # Retrun n is not zero and n is a multiple of m
        return n != 0 and n % m == 0
    # ZeroDivisionError handler
    except ZeroDivisionError:
        return 'Can not divide by zero'
 
def main():
    # Promt the User
    print('This programs takes two numbers (n, m) and determines n is a multiple of m')
    # Accept numbers from keyboard
    n, m = input('Enter two numbers seperated by a space: ').split(' ')
    print(is_multiple(int(n), int(m)))
    
    
main()