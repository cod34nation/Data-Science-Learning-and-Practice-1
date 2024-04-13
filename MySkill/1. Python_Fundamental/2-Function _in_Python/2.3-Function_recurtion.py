# Function Recursive

def factorial(x):
    '''
    this function is calculate factorial number
    '''
    if x == 1:
        return 1
    else:
         return x * factorial(x-1)
    
num = 6

print("Nilai Faktorial dari ", num," adalah ", factorial(num))