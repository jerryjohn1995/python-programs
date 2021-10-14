# Python program to display all the prime numbers within an interval

lower = int(input("Enter the lower value "))
upper = int(input("Enter the upper value "))


print("The prime numbers between {} and {} are ... ".format(lower,upper))
for i in range(lower, upper + 1):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i)
