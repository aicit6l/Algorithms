def fibonacci(fibLimit):
    count = 0
    fibList = [0,1]

    while count < fibLimit:
        count += 1
        for i in range(len(fibList)):
            sum = fibList[i] + fibList[i-1]
        fibList.append(sum)
        
    strFib = ", ".join(map(str, fibList)) # converts each element into a string

    print(fibList)
    print(strFib)


fibonacci(int(input("Enter the fibonacci limit : ")))