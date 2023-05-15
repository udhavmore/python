

def getMultiples(num: int, limit: int):
    multiples = []
    while True:
        if num>limit:
            break
        if num%2==0:
            multiples.append(num)
        num+=1
    return multiples

def getFactors(num: int):
    factors = []
    for i in range(1, num+1):
        if num%i==0:
            factors.append(i)
    return factors
    

def getTotalX(a, b):
    # Write your code here
    # total = 0
    # limit = max(a+b)
    # for i in range(1,limit):
    #     if all(i%x==0 for x in a) and all(y%i==0 for y in b):
    #         total += 1
    # return total

    c = 0
    for i in range(a[-1], b[0] + 1):
        a_factors = list(map(lambda x: i%x, a))
        print(a_factors)
        b_factors = list(map(lambda y: y%i, b))
        print(b_factors)
        
        if sum(a_factors) + sum(b_factors) == 0:
            c +=1
    return c



getTotalX([1],[100])