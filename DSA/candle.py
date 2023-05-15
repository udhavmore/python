def birthdayCakeCandles(candles: list):
    tallest_candle = max(candles)
    count_of_tallest_candle = candles.count(tallest_candle)
    return count_of_tallest_candle


candles = [3, 2, 1, 3]
print(birthdayCakeCandles(candles))
