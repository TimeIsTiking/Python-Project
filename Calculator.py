print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    Choice = input("Pick 1, 2, 3, 4: ")
    if Choice in ("1", "2", "3", "4"):
        num1 = float(input("First Num: "))
        num2 = float(input("Second Num: "))
        if Choice == "1":
            print(num1 + num2)
            
        elif Choice == "2":
            (num1 - num2)
        elif Choice == "3":
            print(num1 * num2)
        elif Choice == "4":
            print(num1 / num2)
        m = input("Do you wish to cointue yes/no: ")
        if m == "no":
            break
    else:
        print("invlaid number")