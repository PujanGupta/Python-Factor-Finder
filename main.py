def findFactorsOf(n):
    factors = []
    for i in range(2, n - 1):
        if n % i == 0:
            factors.append(i)
        else:
            continue
    factors.insert(0, 1)
    factors.append(n)
    
    return factors
    
while True:
    userInput = int(input("Enter a number: "))
    print("The factors of " + str(userInput) + " are: ")
    print(findFactorsOf(userInput))