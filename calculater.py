if __name__=="__main__":
#def cal():
    
    while True:
        a=int(input("enter your first number :"))
        c=input("enter your sign {+,-,*,/}:")
        b=int(input("enter your second number:"))
        print(a,c,b)
        if c == '+':
            print(a+b)
        elif c == '-':
            print(a-b)
        elif c == '*':
            print(a*b)
        elif c == '/':
            print(a/b)
        else:
            print("               !!!!!!!! .please choose correct sign. !!!!!!!!              ")
        d=input(" if you want to close to type (off)\n")
        if d== 'off':
            break
        print("calculater is again started")
print("calculater is closed")
