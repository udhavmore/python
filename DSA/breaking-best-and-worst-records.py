def breakingRecords(scores):
    # Write your code here
    max,min = 0,0
    high, low = scores[0],scores[0]

    for score in scores:
        print(f"score: {score}")
        if score == high and score == low:
            continue
        if score>high:
            print("high")
            high = score
            max += 1
        elif score<low:
            print("low")
            low = score
            min += 1
    return [max, min]


season_scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
season_scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
print(breakingRecords(season_scores))