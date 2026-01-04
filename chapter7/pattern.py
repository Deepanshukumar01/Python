n=int(input("enter the line"))

for i in range(1,n+1):
    print(" "* (n-2*i) ,end="")
    print("*"* (2*i-1),end="")
    print(" ")
 