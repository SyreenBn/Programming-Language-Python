def check(number, x):
    i = 0
    while (number != 0 and number%x == 0):
        number = number/x
        i = i+1
    return i


from_user = input("Please Enter a Number Between 10 and 20 To Check If It Is a PRIME Number or Not: ")
while (int(from_user) < 10 or int(from_user) > 20 ):
    print("Your Number is Out of Range")
    from_user = input("Please Enter a Number Between 10 and 20 To Check If It Is a PRIME Number or Not: ")

user_input = int(from_user)
factor_2 = check(user_input,2)
user_input = user_input/(2**factor_2)
factor_3 = check(user_input,3)
user_input = user_input/(3**factor_3)
factor_5 = check(user_input,5)
user_input = user_input/(5**factor_5)
factor_7 = check(user_input,7)
user_input = user_input/(7**factor_7)

if factor_2 == 0 and factor_3 == 0 and factor_5 == 0 and factor_7 == 0:
    print (from_user, "is a PRIME Number" )
else:
    print("{0} = 2^{1} 3^{2} 5^{3} 7^{4}".format(from_user,factor_2,factor_3,factor_5,factor_7 ))

