n = input("Please Enter Number: ")
print(n)
print(int(0.5*int(n)*(int(n)+1)))
print(int(n)*int(n))


for num in range(2, int(n)):
    if num % 2 == 0:
        print("偶数", num)
    if num % 3 == 0:
        print("ペー", num)
    continue
    print("あほ", num)
