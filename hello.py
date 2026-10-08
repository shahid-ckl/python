a = int(input("Enter a number: "))
while True:
    if(a < 1 or a > 10):
        print("Please enter a number between 1 and 10.")
        a = int(input("Enter a number: "))
    else:
        for i in range(1, 11):
            print(f"{a} x {i} = {a * i}")
        break
