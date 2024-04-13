# Annonymous Function

# Program to Show the use of lamda functions
double = lambda x:x*5
print(double(5))

# If not use annonymous function, but use regular function
def double(x):
    return x*2
print(double(2))


# Program to filter out only the even items from a list

my_list = [1,2,3,4,5,6,7,8,9,10]
new_list = list(filter(lambda x:(x%2==0),my_list))
print(new_list)

# Program to filter out only the even items from a list if using regular function
def even_num(list):
    list_event = []
    for x in list:
        if(x%2==0):
            list_event.append(x)
    print(list_event)

even_num(my_list)

