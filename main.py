num = int(input("Enter a number: "))

n = 1 

if num == 0:
    print(n)
else:
    for i in range(1,num+1):
      n *= i
print(f"The Factorial of the number {num} is",n)      
