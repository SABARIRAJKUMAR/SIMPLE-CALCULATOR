def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a//b
print(""" select operation
1.add
2.sub
3.mul
4.div
""")

choice= int(input("enter yur choice"))
a = int(input("enter num 1"))
b =int(input("enter num 2"))

if choice==1:
    print(add(a,b))
elif choice==2:
    print(sub(a,b))
elif choice==3:
    print(mul(a,b))
elif choice==4:
    print(div(a,b))
else:
    print("please enter crt number")
    #code with ❤ by SABARIRAJKUMAR️
