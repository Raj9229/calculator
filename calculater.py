try:  # Telling the code to not to return error if input of those are strings.

    if __name__ == "__main__":
        # def cal():

        while True:

            a = int(input("enter your first number : "))
            c = input("\nenter your sign {+,-,*,/}: ")
            b = int(input("\nenter your second number: "))

            print(f"\n{a} {c} {b}")
            if c == '+':
                print(a + b)
            elif c == '-':
                print(a - b)
            elif c == '*':
                print(a * b)
            elif c == '/':
                print(a / b)
            else:
                print("               !!!!!!!! .please choose correct sign. !!!!!!!!              ")

            d = input("\nif you want to close to type (off): ")
            if d == 'off':
                break

    print("calculater is closed")

except:             # If the user entered string instead of a integer print the below statement instead of throwing a error.

    print("Enter only integers not strings")
