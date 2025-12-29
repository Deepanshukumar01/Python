a=int(input("enter your annual income:"))

if(a>10000000):
    print("you are rich")
elif(a>3000000):
    print("you are upper middle class")
elif(a>1000000):
    print("you are middle class")
elif(a>500000):
    print("you are lower middle class")
elif(a>=100000):
    print("you are poor")
else:
    print("tumhara kuch nhi ho skta")    
print("done")    