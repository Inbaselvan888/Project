a=int(input("Enter A:"))
b=int(input("Enter B:"))
def swap(x,y):
    global a
    global b
    a=x
    b=y
    a=a+b
    b=a-b
    a=a-b
swap(a,b)
print("A=",a)
print("B=",b)
