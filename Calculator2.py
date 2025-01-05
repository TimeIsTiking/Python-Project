


def multy(x,y):
    x * y
    return x * y
def division(x,y):
    x / y
    return x / y
def substract(x,y):
    x - y
    return x - y
def add(x,y):
    x + y
    return x + y

while True:
    
    print("Type 1 to multy")
    print("Type 2 to add")
    print("Type 3 to substract")
    print("Type 4 to division")
    
    Equatuin = input("")

    num1 = float(input("Put your Number: "))
   
    num2 = float(input("Put your second Number:"))
   
    if Equatuin in ["1","2","3","4"]:
        if Equatuin == "1":
            print(f"{num1} x {num2} = ", multy(num1,num2))
        elif Equatuin == "2":
            print(f"{num1} + {num2} = ", add(num1,num2))
        elif Equatuin == "3":
            print(f"{num1} / {num2} = ", division(num1,num2))
        elif Equatuin == "4":
            print(f"{num1} - {num2} = ", substract(num1,num2))
            
        done = input("Are you done yes/no").startswith("n")
            
    elif done == "n":
        exit()
        
        
        
    else:
        print("Invald Answer")