def countDecreasingRatings(rating: list):
    if len(rating) == 0:
        return "Empty ratings"
    count = 0
    for i in range(len(rating)):
        for j in rating:
            print(j)
            if j > rating[i+1]:
                count += 1
    return count


if __name__ == '__main__':
    ratings = [4,3,5,4,3]
    print(countDecreasingRatings(ratings))
