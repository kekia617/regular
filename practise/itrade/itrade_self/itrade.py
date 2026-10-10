import csv

document = 'stocks.csv'

def load_csv(document):
    stocks = []
    i = True
    with open(document) as file:
        reader = csv.DictReader(file)
        for row in reader:
            stocks.append({"stock_id": row["ID"], 
                        "performance": float(row["Performance"]),
                            "industry": row["Industry"],
                            "foundation_year": int(row["FoundationYear"]),
                            "ESG": (int(row["Environment"])+int(row["Social"])+int(row["Governance"]))//3
                            })
    return stocks

def flitering(stocks):
    stocks_filtered = []
    
    maxium = stocks[0]["ESG"]
    for stock in stocks:
        if maxium == 10:
            break  
        if stock["ESG"] > maxium:
            maxium = stock["ESG"]

    for stock in stocks:
        if stock["ESG"] == maxium:
            stocks_filtered.append(stock)

    return stocks_filtered

def fliter_year(stocks, year):
    stocks_filtered = []
    for stock in stocks:
        if stock["foundation_year"] <= year:
            stocks_filtered.append(stock)
    return stocks_filtered

def fliter_industry(stocks, industry):
    stocks_filtered = []
    for stock in stocks:
        if stock["industry"] == industry:
            stocks_filtered.append(stock)       
    return stocks_filtered

def is_ESG():
    answer = input("do you filter ESG? (yes or no) ")
    if answer == 'yes':
        return True
    else:
        return False
    
def is_year():
    while True:
        try:
            answer = input("do you filter year? (year number(1800 - 2020) or no) ")
            if answer == 'no':
                return False
            elif 1800 <= int(answer) <= 2020:
                return int(answer)
            else:
                return False
        except ValueError:
            print("please answer a number ")
        
def is_industry():
            answer = input("do you filter industry? (industry name or no) ")
            if answer == 'no':
                return False
            else:
                return answer        


def write_csv(stocks):
    n = int(input("How many stocks do you wanna check?(1-100) "))
    with open("stocks_final.csv", 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["ID","Performance","Industry","FoundationYear","ESG"])
        writer.writeheader()

        for stock in sorted(stocks, key=lambda stock: stock["performance"], reverse=True)[:n]:
            writer.writerow({"ID": stock["stock_id"],
                            "Performance": stock["performance"],
                            "Industry": stock["industry"],
                            "FoundationYear": stock["foundation_year"],
                            "ESG": stock["ESG"]})


if __name__ == "__main__":
    stocks = load_csv(document)

    if is_ESG():
        stocks = flitering(stocks)   
    industry = is_industry()
    if industry:
        stocks = fliter_industry(stocks, industry)
    year = is_year()
    if year:
        stocks = fliter_year(stocks, year)

    write_csv(stocks)