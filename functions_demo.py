#### Defination of user defined function with def

def calc():
    print "You are in function - calc()"

def bitcoin_to_usd(btcn):
    amount = btcn * 640
    print amount

def addition(n, m):
    print n+m
calc();
bitcoin_to_usd(100);
bitcoin_to_usd(56);

addition(10, 20);


######  Returning values

def calc(x,y):
    return x+y

sum = calc(13,45)
print sum

#####  Default values for arguments.

## Condition:
    ###  non-default argument should not follows default argument.
def multiply(a, b=1):
    return a*b

def gender(sex='Unknow'):
    if sex is 'm':
        sex = 'male'
    elif sex is 'f':
        sex = 'female'
    return sex

print gender()

print gender('f')
print gender('m')
    
product = multiply(3);
print product
product = multiply(3,5);
print product

product = multiply(12);
print product




