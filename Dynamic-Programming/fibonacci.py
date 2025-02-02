def fibonacci(fibLimit):
    count = 0
    fibList = [0,1]

    while count < fibLimit:
        count += 1
        sum = fibList[-1] + fibList[-2] # accesses the last two computed values and sums them
        fibList.append(sum)
        
    strFib = ", ".join(map(str, fibList)) # converts each element into a string

    print(strFib)


fibonacci(int(input("Enter the fibonacci limit : ")))