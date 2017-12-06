expect_number = int(input("Please enter a number.!"))
print(expect_number)

while True:
    try:
        num = int(input("Enter your favourate number here"))
        print(24/num)
        break
    except:
        print("There is an error, Try again")
        break
    finally:
        print("Loop completed")

