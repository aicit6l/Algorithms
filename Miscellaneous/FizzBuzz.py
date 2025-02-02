def FizzBuzz(num):
    numList = []

    # loop until count reaches num from 1
    count = 0
    while count < num:
        count += 1
        numList.append(count)
    
    #loop through list of results : define-ocg
    for i in range(len(numList)):
        if (numList[i] % 3 == 0 and numList[i] % 5 == 0):
            numList[i] = "FizzBuzz"
        elif numList[i] % 3 == 0:
            numList[i] = "Fizz"
        elif numList[i] % 5 == 0:
            numList[i] = "Buzz"

    #combine results into a string
    result = " ".join(map(str, numList))

    return result

varOcg = FizzBuzz(int(input("Enter a number: ")))

print(varOcg)