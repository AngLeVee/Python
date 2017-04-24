print("enter numbers")
fibonacci = []
fibonacci.append(0)
fibonacci.append(1)
for i in range (1,100):
    fibonacci.append(fibonacci[i-1] + fibonacci[i])
print(fibonacci)
print("Press enter to exit" + input())
