def add_numbers(*numbers):
    total = 0;
    for n in numbers:
        total+=n
    print total

add_numbers(1,2)

add_numbers(2,5,3,4)
add_numbers(2,3,4,5,5,6,7,8,8)

    
    
############ Unpacking arguments

def health_calc(age,apples_ate, cigs_smoked):
    ans = (100-age)+(apples_ate*3.5)-(cigs_smoked *2)
    print ans

my_data = [27, 5, 3]

health_calc(my_data[0], my_data[1], my_data[2])
health_calc(*my_data)
