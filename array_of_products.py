def arrayOfProducts(arr):
    products = [1 for _ in range(len(arr))]

    for i in range(len(arr)):
        runningProduct = 1
        for j in range(len(arr)):
            if i != j:
                runningProduct *= arr[j]
        products[i] = runningProduct

    return products