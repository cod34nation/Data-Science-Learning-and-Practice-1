# Function Argument

def argument (name,msg):
    '''
    this function is basic
    '''
    print("Hello, My Name is "+ name +"I say ",msg)

argument('AFRIZAL', "Good Morning")


# Default Argument in Function

def greet2(name,msg="Good Morning"):
    '''
    This Function give our example use default argument in function parameter
    '''
    print("Hello My Name is "+name+" i say ",msg)

greet2('Octavia')
greet2('Octavia',"Good Afternoon")

# Python Keyword Argument

# 2 Keyword arguments
greet2(name = 'Afrizal', msg="Good Night")

# 2 Keyword Arguments (Out of Order)
greet2(msg="Good Night",name="Afrizal")

#1 positional, 1 keyword argument
greet2('AFRIZAL',msg="Good Night")


#Python Arbitary Arguments

def greet3(*names):
    '''
    this function for greet all people 
    in tupple name
    '''
    for name in names :
        print("Hello," ,name)

greet3('A','B','C')