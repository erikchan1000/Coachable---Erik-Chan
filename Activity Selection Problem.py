testCase1 = [(0, float("inf")), (0, 2), (3, 3)]

testCase2 = [(0, 3), (2, 4), (3, 10)]

def numOfActivities(myArray):
    myArray.sort(key = lambda x : x[-1])

    stack = []

    for x in myArray:
        if not stack:
            stack.append(x)

        elif stack[-1][-1] <= x[0]:
            stack.append(x)

    print(stack)
        
numOfActivities(testCase1)

numOfActivities(testCase2)