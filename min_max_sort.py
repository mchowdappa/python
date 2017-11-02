stocks = {"AMGN":560.67,"FB": 56.78, "GOOGL": 450.78, "YAHO": 67.34}

print(min(zip(stocks.values(), stocks.keys())))

print(max(zip(stocks.values(), stocks.keys())))

print(min(zip(stocks.keys(), stocks.values())))

print(max(zip(stocks.keys(), stocks.values())))

print(sorted(zip(stocks.keys(), stocks.values())))

print(sorted(zip(stocks.values(), stocks.keys())))

