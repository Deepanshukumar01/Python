n = int(input("Enter number of terms: "))

a, b = 0, 1
sum = 0  # Sum track karne ke liye

if n <= 0:
    print("Enter a positive number")
elif n == 1:
    print("Fibonacci sequence:", a)
    print("Sum:", a)
else:
    print("Fibonacci sequence:")
    for i in range(n):
        print(a)
        sum += a  # yaha sum update ho raha hai
        # a, b = b, a + b
        c=a+b
        a=b
        b=c

    print("\nSum of series:", sum)